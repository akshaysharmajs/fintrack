from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.transaction import Transaction
from app.models.budget import Budget
from datetime import datetime

def get_monthly_summary(db: Session, user_id: int):
    current_month_start = datetime(datetime.utcnow().year, datetime.utcnow().month, 1)
    # Sum transactions by category
    result = db.query(
        Transaction.category,
        func.sum(Transaction.amount).label("total_spent")
    ).filter(
        Transaction.user_id == user_id,
        Transaction.timestamp >= current_month_start
    ).group_by(Transaction.category).all()

    # Fetch budgets
    budgets = db.query(Budget).filter(Budget.user_id == user_id).all()
    budget_map = {b.category: b.monthly_limit for b in budgets}

    summary = []
    for category, total_spent in result:
        summary.append({
            "category": category,
            "spent": float(total_spent),
            "budget": budget_map.get(category, None),
            "over_limit": budget_map.get(category, 0) < float(total_spent) if category in budget_map else False
        })

    return summary
