from fastapi import APIRouter

router = APIRouter(prefix="/journal")


@router.get("/")
async def home():
    return "Journal"
