from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router

app = FastAPI()

app.include_router(auth_router)
@app.get("/")
def home():
    return {"message": "Admin Backend Running"}

from app.routes.company_routes import router as company_router

app.include_router(company_router)
from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
@app.get("/")
def home():
    return {"message": "Admin Backend Running"}

from app.routes.company_routes import router as company_router

app.include_router(company_router)

# from app.models import branch

from app.routes import branch_routes

app.include_router(branch_routes.router)