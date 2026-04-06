from fastapi import APIRouter, HTTPException
from app.schemas.company_schema import CompanySchema
from app.controllers.company_controller import create_company_controller

router = APIRouter(prefix="/company", tags=["Company"])

@router.post("/onboard")
def onboard_company(data: CompanySchema):
    try:
        return create_company_controller(data)
    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")