python
# src/services/auth.py
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from src.utils import secret_key, algorithm

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: str

pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

secret = secret_key
algo = algorithm

manager = LoginManager(secret=secret, token_url="/auth/token", use_absolute_url=True)

# Token validation
def validate_token(token: str = Depends(manager)):
    return True

# Get current user
def get_current_user(token: str = Depends(manager)):
    return {"id": 1, "username": "admin", "email": "admin@example.com"}

# Register user
app.post("/register", status_code=201)
async def register(user: User):
    user_in_db = User.parse_obj(user)
    hashed_password = pwd_context.hash(user_in_db.password)
    user_in_db.password = hashed_password
    return user_in_db

# Login user
app.post("/auth/token", response_model=User)
async def login(data: OAuth2PasswordRequestForm = Depends()):
    user = await db.get_user(data.username)
    if not user or not pwd_context.verify(data.password, user.password):
        raise HTTPException(401, "Incorrect username or password")
    access_token_expires = timedelta(minutes=timedelta.total_seconds(30))
    access_token = jwt.encode(
        {"exp": datetime.utcnow() + access_token_expires,
         "sub": user.id}, secret, algorithm
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Protected route
@app.get("/protected")
async def protected_route(current_user: dict = Depends(validate_token)):
    return current_user


# Note: db.get_user() and OAuth2PasswordRequestForm() have been left for implementation
# as they depend on the project setup and database structure.
