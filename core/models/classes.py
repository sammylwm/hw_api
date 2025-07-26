from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Classes(Base):
    class_name: Mapped[str] = mapped_column(unique=True)
    schedule: Mapped[dict] = mapped_column(JSON)
    homeworks: Mapped[dict] = mapped_column(JSON)
    owner: Mapped[str]
    admins: Mapped[list] = mapped_column(JSON)
