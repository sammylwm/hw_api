from sqlalchemy import JSON
from sqlalchemy.ext.mutable import MutableDict, MutableList
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Classes(Base):
    class_name: Mapped[str] = mapped_column(primary_key=True)
    homeworks: Mapped[dict] = mapped_column(MutableDict.as_mutable(JSON))
    owner: Mapped[str]
    admins: Mapped[list] = mapped_column(MutableList.as_mutable(JSON))
