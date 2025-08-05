from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import RegisterData, Register

router = APIRouter(tags=["Register"])

@router.get("/", response_model=list[Register])
async def get_registers(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_registers(session=session)


@router.post("/", response_model=int)
async def reg(data: RegisterData,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.send_code(session, data.email)