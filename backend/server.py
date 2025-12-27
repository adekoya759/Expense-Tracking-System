from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database")

    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses updated successfully"}


from collections import defaultdict
from datetime import datetime

@app.post("/analytics")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database")

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }
    return breakdown



@app.post("/analytics/monthly")
def get_total_monthly_expenses():
    data = db_helper.fetch_all_records()

    if not data:
        return {}

    monthly_totals = defaultdict(float)

    for row in data:
        expense_date = row.get("expense_date")
        amount = row.get("amount", 0)

        if not expense_date:
            continue

        if isinstance(expense_date, str):
            expense_date = datetime.strptime(expense_date, "%Y-%m-%d")

        month_key = expense_date.strftime("%Y-%m")
        monthly_totals[month_key] += amount

    return dict(monthly_totals)