from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.db_helper import db_helper

from . import crud
from .dependencies import get_product_by_id
from .schemas import Product, ProductBase, ProductCreate

router = APIRouter()


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_single_product(
    product: Product = Depends(get_product_by_id),
):
    return product


@router.post("/", response_model=ProductBase)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)
