from jose import jwt
from app.core.config import JWT_SECRET

def create_token(data: dict):
    return jwt.encode(data, JWT_SECRET, algorithm="HS256")