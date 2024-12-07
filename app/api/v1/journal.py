from fastapi import APIRouter
from services.journal_service import JournalService
from schema.entry import Entry

router = APIRouter()


@router.get("/")
async def home():
    return "Journal"

@router.post("/")
async def create(content):
    return JournalService().post_entry(content)
    return Entry(entry_id=1, content="I had a good day!")
