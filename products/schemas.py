from pydantic import BaseModel, ConfigDict

from users.schemas import UserBase, User


class CategoryBase(BaseModel):
    title: str
    description: str


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ProductBase(BaseModel):
    title: str
    description: str
    city: str
    price: int
    currency: str
    category: Category
    user: User


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
