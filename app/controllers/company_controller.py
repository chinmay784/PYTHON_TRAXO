from app.utils.db_helpers import create_company

def create_company_controller(data):
    company_data = data.dict()
    create_company(company_data)
    return {"message": "Company onboarded successfully"}