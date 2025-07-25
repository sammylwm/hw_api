from fastapi import APIRouter
from api.users import crud
from api.users.schemas import CreateUser

router = APIRouter(prefix="/users")


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
