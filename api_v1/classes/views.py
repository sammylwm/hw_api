from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import (
    Classes,
    CheckAdmin,
    CheckLes,
    AddHw,
    GetHw,
    GetMembers,
    AdminAction,
)

router = APIRouter(tags=["Classes"])


@router.get("/", response_model=list[Classes])
async def get_classes(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_all(session=session)


@router.post("/check_admin/", response_model=int)
async def check_admin(
    data: CheckAdmin,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.check_admin(session, data.class_name, data.email)





@router.post("/less_in_day/", response_model=int)
async def less_in_day(data: CheckLes):
    return await crud.less_in_day(data.class_name, data.subject, data.weekday)


@router.post("/add_hw/", response_model=int)
async def add_hw(
    data: AddHw,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.add_hw(session, data.class_name, data.subject, data.date, data.hw)


@router.post("/get_hw/", response_model=list)
async def get_hw(
    data: GetHw,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_hw(session, data.class_name, data.date)


@router.post("/get_members/", response_model=dict)
async def get_members(
    data: GetMembers,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_admins(session, data.class_name)


@router.post("/add_admin/", response_model=int)
async def add_admin(
    data: AdminAction,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.add_admin(session, data.class_name, data.email)


@router.post("/del_admin/", response_model=int)
async def del_admin(
    data: AdminAction,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.del_admin(session, data.class_name, data.email)
