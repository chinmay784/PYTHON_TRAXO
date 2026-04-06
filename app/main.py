from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router

app = FastAPI()

app.include_router(auth_router)
@app.get("/")
def home():
    return {"message": "Admin Backend Running"}

from app.routes.company_routes import router as company_router

app.include_router(company_router)