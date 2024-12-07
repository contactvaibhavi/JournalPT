from fastapi import APIRouter
from services.authentication import AuthenticationService

router = APIRouter()


@router.get("/")
async def home():
    return "auth"


@router.get("/login")
async def login():
    return "you're logged in"

@router.get("/profile")
async def profile():
    return AuthenticationService().get_user(1)