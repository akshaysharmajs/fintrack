from pydantic import BaseModel

class BudgetCreate(BaseModel):
    category: str
    monthly_limit: float

class BudgetOut(BudgetCreate):
    id: int

    class Config:
        orm_mode = True
