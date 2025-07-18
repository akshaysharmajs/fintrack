# init_db.py
from app.database import Base, engine
from app.models import user, transaction, budget  # ensures all relationships resolve


print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
