from pydantic import BaseModel, ConfigDict
from typing import Optional


class ClassesBase(BaseModel):
    class_name: str
    schedule: dict
    homeworks: dict
    owner: str
    admins: list


class ClassesCreate(ClassesBase):
    pass

class ClassesUpdate(ClassesCreate):
    pass

class ClassesUpdatePartial(BaseModel):
    class_name: Optional[str] = None
    schedule: Optional[dict] = None
    homeworks: Optional[dict] = None
    owner: Optional[str] = None
    admins: Optional[list] = None


class Classes(ClassesBase):
    model_config = ConfigDict(from_attributes=True)

class CheckAdmin(BaseModel):
    class_name: str
    email: str

class CheckLes(BaseModel):
    class_name: str
    subject: str
    weekday: str

class AddHw(BaseModel):
    hw: str
    subject: str
    date: str
    class_name: str

class GetHw(BaseModel):
    date: str
    class_name: str