from fastapi import APIRouter
from .v1 import auth, embedding, journal, llm

router = APIRouter(prefix="/v1")


@router.get("/")
async def home():
    return "Router"


router.include_router(auth.router, prefix="/auth")
router.include_router(embedding.router, prefix="/embedding")
router.include_router(journal.router, prefix="/journal")
router.include_router(llm.router, prefix="/llm")
