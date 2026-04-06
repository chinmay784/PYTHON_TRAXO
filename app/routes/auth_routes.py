



# from fastapi import APIRouter, HTTPException
# from app.schemas.auth_schema import RegisterSchema, LoginSchema
# from app.controllers.auth_controller import register_controller, login_controller
# from app.schemas.password_schema import ForgotPasswordSchema, ResetPasswordSchema
# from app.utils.db_helpers import get_user_by_email, get_user_by_token, update_user
# from app.utils.hash import hash_password
# from app.utils.token import generate_reset_token
# # from app.utils.email import send_reset_email   # keep off for now

# router = APIRouter(prefix="/auth", tags=["Auth"])


# @router.post("/register")
# def register(data: RegisterSchema):
#     return register_controller(data)


# @router.post("/login")
# def login(data: LoginSchema):
#     return login_controller(data)

# @router.post("/forgot-password")
# def forgot_password(data: ForgotPasswordSchema):
#     try:
#         print("🔥 API HIT")
#         print("Email:", data.email)

#         user = get_user_by_email(data.email)
#         print("User found:", user)

#         if not user:
#             raise HTTPException(status_code=404, detail="User not found")

#         token = generate_reset_token()
#         print("Token:", token)

#         update_user(
#             {"email": data.email},
#             {"reset_token": token}
#         )

#         return {
#             "message": "Reset token generated",
#             "token": token
#         }

#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.post("/reset-password")
# def reset_password(data: ResetPasswordSchema):
#     try:
#         user = get_user_by_token(data.token)

#         if not user:
#             raise HTTPException(status_code=400, detail="Invalid token")

#         hashed_password = hash_password(data.new_password)

#         update_user(
#             {"reset_token": data.token},
#             {
#                 "password": hashed_password,
#                 "reset_token": None
#             }
#         )

#         return {"message": "Password updated successfully"}

#     except Exception as e:
#         print("ERROR:", str(e))
#         raise HTTPException(status_code=500, detail="Internal Server Error")





from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import RegisterSchema, LoginSchema
from app.controllers.auth_controller import register_controller, login_controller
from app.schemas.password_schema import ForgotPasswordSchema, ResetPasswordSchema
from app.utils.db_helpers import get_user_by_email, get_user_by_token, update_user
from app.utils.hash import hash_password
from app.utils.token import generate_reset_token
import logging

router = APIRouter(prefix="/auth", tags=["Auth"])

logger = logging.getLogger(__name__)


# ✅ REGISTER
@router.post("/register")
def register(data: RegisterSchema):
    try:
        result = register_controller(data)
        return {
            "success": True,
            "data": result
        }
    except Exception as e:
        logger.error(f"Register Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Registration failed")


# ✅ LOGIN
@router.post("/login")
def login(data: LoginSchema):
    try:
        result = login_controller(data)
        return {
            "success": True,
            "data": result
        }
    except Exception as e:
        logger.error(f"Login Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Login failed")


# ✅ FORGOT PASSWORD
@router.post("/forgot-password")
def forgot_password(data: ForgotPasswordSchema):
    try:
        user = get_user_by_email(data.email)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        token = generate_reset_token()

        update_user(
            {"email": data.email},
            {"reset_token": token}
        )

        return {
            "success": True,
            "message": "Reset token generated",
            "token": token
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Forgot Password Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# ✅ RESET PASSWORD
@router.post("/reset-password")
def reset_password(data: ResetPasswordSchema):
    try:
        user = get_user_by_token(data.token)

        if not user:
            raise HTTPException(status_code=400, detail="Invalid token")

        hashed_password = hash_password(data.new_password)

        update_user(
            {"reset_token": data.token},
            {
                "password": hashed_password,
                "reset_token": None
            }
        )

        return {
            "success": True,
            "message": "Password updated successfully"
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Reset Password Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")