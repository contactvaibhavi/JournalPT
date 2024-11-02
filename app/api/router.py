from fastapi import APIRouter
from .v1 import auth, embedding, journal, llm

router = APIRouter(prefix="/api")


@router.get("/")
async def home():
    return "Router"


router.include_router(auth.router)
router.include_router(embedding.router)
router.include_router(journal.router)
router.include_router(llm.router)
