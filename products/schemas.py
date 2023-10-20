from pydantic import BaseModel, ConfigDict

from users.schemas import UserBase


class CategoryBase(BaseModel):
    id: int
    title: str
    description: str


class ProductBase(BaseModel):
    title: str
    description: str
    city: str
    price: int
    currency: str
    category: CategoryBase
    user: UserBase


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
