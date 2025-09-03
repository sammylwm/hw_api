from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud

router = APIRouter(tags=["Register"])


class RegisterData(BaseModel):
    email: str


@router.post("/", response_model=int)
async def reg(
    data: RegisterData,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.send_code(session, data.email)
