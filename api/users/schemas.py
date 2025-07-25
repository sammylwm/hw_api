from pydantic import BaseModel


class CreateUser(BaseModel):
    email: str
    password: str
    login_dn: str
    password_dn: str
