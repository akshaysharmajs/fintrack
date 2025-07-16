from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    amount: float
    category: str
    description: str = ""

class TransactionOut(TransactionCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
