from sqlalchemy import String, Enum, Numeric, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.models import Base
from core.database.models.mixins import UserRelationMixin

CURRENCY_CHOICES = ("Сом", "USD")


class Category(Base):
    title: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(100))
    parent_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"), nullable=True)
    children: Mapped["Category"] = relationship("Category")
    products: Mapped[list["Product"]] = relationship(back_populates="category")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r})"

    def __repr__(self):
        return str(self)

class Product(UserRelationMixin, Base):
    _user_id_unique = False
    _user_back_populates = "product"

    title: Mapped[str] = mapped_column(String(60))
    description: Mapped[str] = mapped_column(String(300))
    city: Mapped[str] = mapped_column(String(20))
    price: Mapped[int] = mapped_column(Numeric(8, 0))
    currency: Mapped[str] = mapped_column(
        Enum(*CURRENCY_CHOICES, name="Currency choices")
    )
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="category")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r})"

    def __repr__(self):
        return str(self)
