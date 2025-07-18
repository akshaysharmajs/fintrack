from fastapi import APIRouter
from app.api import auth, transactions, budgets
from app.api import summary

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
router.include_router(budgets.router, prefix="/budgets", tags=["budgets"])
router.include_router(summary.router, prefix="/summary", tags=["summary"])
