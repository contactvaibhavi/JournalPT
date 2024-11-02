from fastapi import APIRouter

from schema.user import User
from services.authentication import AuthenticationService

router = APIRouter(prefix="/auth")


@router.get("/")
async def home():
    return "auth"


@router.get("/login")
async def login():
    return "you're logged in"

@router.get("/profile")
async def profile():
    return AuthenticationService().get_user()