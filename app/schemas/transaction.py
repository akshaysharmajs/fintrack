from pydantic import BaseModel, Field
from datetime import datetime

class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Transaction amount must be > 0")
    category: str = Field("", description="Leave blank for auto-categorization")
    description: str = Field(..., min_length=1)

class TransactionOut(TransactionCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
