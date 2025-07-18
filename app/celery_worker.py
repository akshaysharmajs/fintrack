from celery import Celery
import os
from app.models import user, transaction, budget  # ensures all relationships resolve


REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

celery_app = Celery("fintrack", broker=REDIS_URL)

@celery_app.task
def categorize_transaction_task(tx_id: int):
    from app.services.categorization import categorize_transaction
    categorize_transaction(tx_id)

@celery_app.task
def check_budget_alerts(user_id: int):
    from app.database import SessionLocal
    from app.crud.summary import get_monthly_summary

    db = SessionLocal()
    try:
        summary = get_monthly_summary(db, user_id)
        alerts = [item for item in summary if item["over_limit"]]
        if alerts:
            print(f"Budget Alerts for user {user_id}: {alerts}")
            # Later: send email or push notification
    finally:
        db.close()
