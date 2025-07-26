from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.marks import parsing
from core.models import db_helper
from pydantic import BaseModel, ConfigDict
from typing import Optional

class CheckData(BaseModel):
    login: str
    password: str

router = APIRouter(tags=["Marks"])

@router.post("/check/")
async def check_lp(data: CheckData):
    res = await parsing.log_ps(data.login, data.password)
    if res:
        return 1
    else:
        return 0

@router.post("/")
async def get_marks(data: CheckData):
    res = await parsing.parse(data.login, data.password)
    return res

@router.post("/all/")
async def get_all_marks(data: CheckData):
    res = await parsing.parse_all(data.login, data.password)
    return res