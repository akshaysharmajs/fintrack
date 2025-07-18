from fastapi import FastAPI
from app.api import router as api_router
from fastapi.responses import RedirectResponse

app = FastAPI(title="FinTrack: Expense Management")

app.include_router(api_router)


@app.get("/")
def root():
    return RedirectResponse(url="/docs")