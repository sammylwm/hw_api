from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    email: str
    password: str
    login_dn: str
    password_dn: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):
    email: str | None = None
    password: str | None = None
    login_dn: str | None = None
    login_password: str | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int