import datetime
from fastapi import APIRouter
from pydantic import BaseModel

from  services.llm import LlmService
router = APIRouter()


@router.get("/")
async def home():
    return "LLM"

class SummaryRequest(BaseModel):
    user_id: int
    days: list[str]

@router.post("/summarise")
async def summarise(summary_request: SummaryRequest):
    dates = [datetime.datetime.strptime(day, "%Y-%m-%d").date() for day in summary_request.days]
    return LlmService().summarise_entrys(summary_request.user_id, dates)

@router.get("/aigenerated")
async def aigenerated(aigen_id: int):
    return LlmService().get_aigen_by_id(aigen_id)

@router.get("/calls")
async def calls(limit=10, skip=0):
    return LlmService().get_llm_calls(limit, skip)
