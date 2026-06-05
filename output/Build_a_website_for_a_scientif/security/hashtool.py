python
# security/hashtool.py

import hashlib
import secrets

class HashTool:
    def __init__(self):
        self.salt_size = 32  # size of salt in bytes

    def generate_salt(self) -> bytes:
        return secrets.token_bytes(self.salt_size)

    def hash_password(self, password: str, salt: bytes) -> tuple:
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    def verify_password(self, password: str, stored_hash: tuple) -> bool:
        hashed_password, stored_salt = stored_hash
        return self.hash_password(password, stored_salt) == hashed_password

    def create_password_hash(self, password: str) -> tuple:
        salt = self.generate_salt()
        hashed_password = self.hash_password(password, salt)
        return salt, hashed_password

def main():
    hash_tool = HashTool()
    password = "mysecretpassword"
    salt, hashed_password = hash_tool.create_password_hash(password)
    print(f"Salt: {salt.hex()}")
    print(f"Hashed Password: {hashed_password.hex()}")

    print(f"Verification: {hash_tool.verify_password(password, (hashed_password, salt))}")

if __name__ == "__main__":
    main()



# security/model.py

from typing import Optional
from security.hashtool import HashTool
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, index=True)
    password = Column(String(50))

    @property
    def password_hash(self):
        return self.password.split(':')

    @password_hash.setter
    def password_hash(self, value):
        hash_tool = HashTool()
        salt, hashed_password = value
        self.password = f"{salt}:{hashed_password.hex()}"

    def verify_password(self, password: str) -> bool:
        hash_tool = HashTool()
        salt, stored_hash = self.password_hash
        return hash_tool.verify_password(password, (stored_hash, salt))

class Formula(Base):
    __tablename__ = "formulas"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    content = Column(String(500), nullable=False)

    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content

class CalculationHistory(Base):
    __tablename__ = "calculation_history"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    formula_id = Column(Integer, ForeignKey('formulas.id'), nullable=False)
    timestamp = Column(Integer, nullable=False)
    values = Column(String(500), nullable=False)

class DatabaseManager:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def create_user(self, username: str, password: str):
        session = self.Session()
        user = User(username=username, password_hash=(secrets.token_bytes(32), secrets.token_bytes(32)))
        session.add(user)
        session.commit()
        return user

    def get_user(self, username: str) -> Optional[User]:
        session = self.Session()
        user = session.query(User).filter(User.username == username).first()
        return user

    def save_formula(self, user_id: int, name: str, content: str):
        session = self.Session()
        formula = Formula(name, content)
        session.add(formula)
        session.commit()

    def get_formula(self, formula_id: int) -> Optional[Formula]:
        session = self.Session()
        formula = session.query(Formula).filter(Formula.id == formula_id).first()
        return formula

    def save_calculation_history(self, user_id: int, formula_id: int, values: str):
        session = self.Session()
        calculation_history = CalculationHistory(user_id=user_id, formula_id=formula_id, timestamp=int(time.time()), values=values)
        session.add(calculation_history)
        session.commit()
