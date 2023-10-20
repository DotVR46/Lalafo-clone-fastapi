from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.database.models import Product
from .schemas import ProductBase


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).options(joinedload(Product.category), joinedload(Product.user)).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)
