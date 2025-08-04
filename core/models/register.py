from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Register(Base):
    email: Mapped[str] = mapped_column(unique=True, primary_key=True)
    code: Mapped[int]
