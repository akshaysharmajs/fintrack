from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.summary import get_monthly_summary
from app.deps import get_db

router = APIRouter()

@router.get("/")
def get_summary(
    db: Session = Depends(get_db),
    user_id: int = 1
):
    return get_monthly_summary(db, user_id)
