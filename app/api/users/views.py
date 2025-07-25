from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import user
from .schemas import User, UserCreate
from app.database.models import db_helper

router = APIRouter(tags=["User"])


@router.get("/", response_model=list[User])
async def get_users(
    session: AsyncSession = Depends(
        db_helper.session_dependency,
    ),
):
    return await user.get_users(session)


@router.get("/create", response_model=User)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(
        db_helper.session_dependency,
    ),
):
    return await user.created_user(session, user_in)


@router.get("/{user_id}/", response_model=User)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(
        db_helper.session_dependency,
    ),
):
    user_res = await user.get_user(session, user_id=user_id)
    if user_res is not None:
        return user_res
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"{user_id} not found"
    )
