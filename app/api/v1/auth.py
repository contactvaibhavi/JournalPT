from fastapi import APIRouter
from services.authentication import AuthenticationService
from pydantic import BaseModel

router = APIRouter()


@router.get("/")
async def home():
    return "auth"

class UserRequest(BaseModel):
    user_name: str
    user_age: int
    user_password: str
    user_email: str

@router.post("/register")
async def register(user: UserRequest):
    user_id = AuthenticationService().create_user(
        user_password=user.user_password,
        user_email=user.user_email,
        user_age=user.user_age, 
        user_name=user.user_name
    )
    return user_id

@router.get("/login")
async def login():
    return "you're logged in"

@router.get("/profile")
async def profile(user_email: str):
    return AuthenticationService().get_user(user_email)