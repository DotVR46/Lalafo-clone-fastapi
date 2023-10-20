from pydantic import BaseModel


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
