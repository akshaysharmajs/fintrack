# init_db.py
from app.database import Base, engine
from app.models import user, transaction, budget

Base.metadata.create_all(bind=engine)
