import datetime
from fastapi import APIRouter
from pydantic import BaseModel
from services.journal import JournalService

router = APIRouter()


@router.get("/")
async def home():
    return "Journal"

class EntryRequest(BaseModel):
    user_id: int
    content: str
    date: str

@router.post("/create")
async def create(entry: EntryRequest):
    date = datetime.datetime.strptime(entry.date, "%Y-%m-%d").date()
    entry_id = JournalService().post_entry(entry.user_id, entry.content, date)
    return entry_id

@router.get("/read")
async def read(user_id: int):
    return JournalService().get_entrys_by_user_id(user_id)