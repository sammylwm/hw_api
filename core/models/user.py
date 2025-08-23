from sqlalchemy import JSON, BIGINT, String, BigInteger
from sqlalchemy.ext.mutable import MutableDict, MutableList
from sqlalchemy.orm import Mapped, mapped_column


from .base import Base


class User(Base):
    email: Mapped[str] = mapped_column(String(255), unique=True, primary_key=True)
    class_name: Mapped[str] = mapped_column(String(255), default="DefaultClass")
    password: Mapped[str] = mapped_column(String(255))
    login_dn: Mapped[str] = mapped_column(String(255))
    password_dn: Mapped[str] = mapped_column(String(255))
    uid: Mapped[int] = mapped_column(BigInteger, default=0)