from fastapi import APIRouter
from app.api import auth, transactions, budgets

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
router.include_router(budgets.router, prefix="/budgets", tags=["budgets"])
