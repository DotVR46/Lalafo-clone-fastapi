from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.database.models import Product, Category
from .schemas import ProductBase, ProductCreate


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = (
        select(Product)
        .options(joinedload(Product.category), joinedload(Product.user))
        .order_by(Product.id)
    )
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_single_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(
        Product,
        product_id,
        options=(joinedload(Product.category), joinedload(Product.user)),
    )


async def create_product(session: AsyncSession, product_in: ProductCreate):
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product