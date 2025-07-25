from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    __tablename__ = "users"
    email: str
    password: str
    login_dn: str
    password_dn: str


class UserCreate(BaseModel):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
