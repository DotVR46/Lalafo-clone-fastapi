from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    description: str
    city: str
    price: int
    currency: str
    category_id: int
