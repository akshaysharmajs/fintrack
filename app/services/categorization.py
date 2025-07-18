from app.database import SessionLocal
from app.models.transaction import Transaction

CATEGORY_RULES = {
    "uber": "Transport",
    "ola": "Transport",
    "swiggy": "Food",
    "zomato": "Food",
    "rent": "Housing",
    "grocery": "Groceries",
    "amazon": "Shopping"
}

def categorize_transaction(tx_id: int):
    db = SessionLocal()
    try:
        tx = db.query(Transaction).filter(Transaction.id == tx_id).first()
        if not tx or tx.category:  # already categorized
            return

        desc = tx.description.lower()
        for keyword, category in CATEGORY_RULES.items():
            if keyword in desc:
                tx.category = category
                db.commit()
                break
    finally:
        db.close()
