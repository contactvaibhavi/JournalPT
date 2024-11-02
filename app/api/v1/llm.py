from fastapi import APIRouter

router = APIRouter(prefix="/llm")


@router.get("/")
async def home():
    return "LLM"
