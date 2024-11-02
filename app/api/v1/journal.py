from fastapi import APIRouter
from schema.entry import Entry

router = APIRouter(prefix="/journal")


@router.get("/")
async def home():
    return "Journal"

@router.post("/")
async def create():
    return Entry(entry_id=1, content="I had a good day!")
