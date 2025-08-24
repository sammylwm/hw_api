from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from crypto import encrypt, unencrypt
from core.models import db_helper
from . import crud
from .schemas import User, UserCreate, LoginData, GetDatas
from ..classes.crud import get_classes, create_info_class

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[User])
async def get_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_users(session=session)


@router.post("/", response_model=int)
async def user_exists(data: LoginData,
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                      ):
    return await crud.user_exists(session, data.email, data.password)


@router.post("/get_datas/", response_model=list)
async def user_exists(data: GetDatas,
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                      ):
    return await crud.get_log_passw_class(session, data.email)


@router.post("/web_get_datas/", response_model=list)
async def user_exists(data: GetDatas,
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                      ):
    return await crud.get_log_passw_class(session, encrypt(data.email))


@router.post(
    "/create/",
    response_model=bool,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
        user_in: UserCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    class_ = await get_classes(session, user_in.class_name)
    if class_ is None:
        await create_info_class(session, user_in.class_name, user_in.email)
    return await crud.create_user(session=session, user_in=user_in)


@router.post("/del/")
async def delete_user(data: GetDatas,
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                      ) -> None:
    await crud.delete_user(session=session, email=data.email)
