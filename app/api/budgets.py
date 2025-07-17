from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.budget import BudgetCreate, BudgetOut
from app.crud.budget import set_budget, get_user_budgets
from app.deps import get_db

router = APIRouter()

@router.post("/", response_model=BudgetOut)
def create_or_update_budget(
    budget: BudgetCreate,
    db: Session = Depends(get_db),
    user_id: int = 1
):
    return set_budget(db, user_id, budget)

@router.get("/", response_model=list[BudgetOut])
def list_user_budgets(
    db: Session = Depends(get_db),
    user_id: int = 1
):
    return get_user_budgets(db, user_id)
