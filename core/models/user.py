from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    email: Mapped[str] = mapped_column(unique=True, primary_key=True)
    class_name: Mapped[str] = mapped_column(default="DefaultClass")
    password: Mapped[str]
    login_dn: Mapped[str]
    password_dn: Mapped[str]
