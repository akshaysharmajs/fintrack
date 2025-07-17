from sqlalchemy.orm import Session
from app.models.budget import Budget
from app.schemas.budget import BudgetCreate

def set_budget(db: Session, user_id: int, data: BudgetCreate):
    budget = db.query(Budget).filter(
        Budget.user_id == user_id, Budget.category == data.category
    ).first()
    
    if budget:
        budget.monthly_limit = data.monthly_limit
    else:
        budget = Budget(**data.dict(), user_id=user_id)
        db.add(budget)

    db.commit()
    db.refresh(budget)
    return budget

def get_user_budgets(db: Session, user_id: int):
    return db.query(Budget).filter(Budget.user_id == user_id).all()
