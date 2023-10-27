from typing import Literal
from pydantic import BaseModel, ConfigDict

from users.schemas import UserBase, User


class CategoryBase(BaseModel):
    title: str
    description: str
    parent_id: int | None


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProductBase(BaseModel):

    title: str
    description: str
    city: str
    price: int
    currency: Literal["Сом", "USD"]
    # category: Category
    # user: User


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    category: Category
    user: User
    id: int


class ProductCreate(ProductBase):
    category_id: int
    user_id: int
