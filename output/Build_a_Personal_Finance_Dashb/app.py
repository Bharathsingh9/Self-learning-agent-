import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    category: str
    amount: float

expenses = []

@app.post('/add_expense')
async def add_expense(expense: Expense):
    global expenses
    expenses.append(expense.dict())
    return expense.dict()

@app.get('/get_expenses')
async def get_expenses():
    return expenses

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)