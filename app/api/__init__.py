from fastapi import APIRouter
from app.api import auth  # will add more later

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["auth"])
