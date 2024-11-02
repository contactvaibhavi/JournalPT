from fastapi import APIRouter

router = APIRouter(prefix="/embedding")


@router.get("/")
async def home():
    return "Embedding"
