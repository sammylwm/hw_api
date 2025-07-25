from sqlalchemy.orm import Mapped

from .base import Base


class User(Base):
    __tablename__ = "users"
    email: Mapped[str]
    password: Mapped[str]
    login_dn: Mapped[str]
    password_dn: Mapped[str]
