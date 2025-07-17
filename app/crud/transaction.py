from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate

def create_transaction(db: Session, user_id: int, tx_data: TransactionCreate):
    tx = Transaction(**tx_data.dict(), user_id=user_id)
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

def get_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()
