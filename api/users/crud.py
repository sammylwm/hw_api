"""
create
read
update
delete
"""

from api.users.schemas import CreateUser


def create_user(user_in: CreateUser):
    user = user_in.model_dump()
    return {
        "message": "True",
        "user": user,
    }
