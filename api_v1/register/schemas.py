from pydantic import BaseModel, ConfigDict


class RegisterBase(BaseModel):
    email: str
    code: str

class RegisterCreate(RegisterBase):
    pass

class Register(RegisterBase):
    model_config = ConfigDict(from_attributes=True)

class RegisterData:
    email: str