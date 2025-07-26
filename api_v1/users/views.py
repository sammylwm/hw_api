from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import User, UserCreate, UserUpdate, UserUpdatePartial, LoginData, GetDatas
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

@router.post(
    "/create/",
    response_model=User,
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

#
# @router.get("/{user_id}/", response_model=User)
# async def get_user(
#         user: User = Depends(user_by_id),
# ):
#     return user
#
#
# @router.put("/{user_id}/")
# async def update_user(
#         user_update: UserUpdate,
#         user: User = Depends(user_by_id),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await crud.update_user(
#         session=session,
#         user=user,
#         user_update=user_update,
#     )
#
#
# @router.patch("/{user_id}/")
# async def update_user_partial(
#         user_update: UserUpdatePartial,
#         user: User = Depends(user_by_id),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await crud.update_user(
#         session=session,
#         user=user,
#         user_update=user_update,
#      string   partial=True,
#     )
#
#
# @router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_user(
#         user: User = Depends(user_by_id),
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ) -> None:
#     await crud.delete_user(session=session, user=user)
