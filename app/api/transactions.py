from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.transaction import TransactionCreate, TransactionOut
from app.crud.transaction import create_transaction, get_transactions
from app.deps import get_db
from app.celery_worker import categorize_transaction_task
from app.celery_worker import categorize_transaction_task, check_budget_alerts

router = APIRouter()


@router.post("/", response_model=TransactionOut)
def add_transaction(
    tx: TransactionCreate,
    db: Session = Depends(get_db),
    user_id: int = 1
):
    new_tx = create_transaction(db, user_id, tx)
    categorize_transaction_task.delay(new_tx.id)
    return new_tx


@router.get("/", response_model=list[TransactionOut])
def list_transactions(
    db: Session = Depends(get_db),
    user_id: int = 1
):
    return get_transactions(db, user_id)

@router.post("/", response_model=TransactionOut)
def add_transaction(
    tx: TransactionCreate,
    db: Session = Depends(get_db),
    user_id: int = 1
):
    new_tx = create_transaction(db, user_id, tx)
    categorize_transaction_task.delay(new_tx.id)
    check_budget_alerts.delay(user_id)
    return new_tx
