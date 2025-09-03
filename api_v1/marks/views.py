from fastapi import APIRouter
from api_v1.marks import parsing
from pydantic import BaseModel
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