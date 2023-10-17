from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.models import Base

if TYPE_CHECKING:
    from .product import Product


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(String(32), unique=True)
    phone: Mapped[str] = mapped_column(String(12), unique=True)
    bio: Mapped[str | None]

    products: Mapped[list["Product"]] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)
