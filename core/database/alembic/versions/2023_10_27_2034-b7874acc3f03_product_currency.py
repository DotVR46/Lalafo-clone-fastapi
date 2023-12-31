"""Product.currency

Revision ID: b7874acc3f03
Revises: 58ef9d675da4
Create Date: 2023-10-27 20:34:25.716942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "b7874acc3f03"
down_revision: Union[str, None] = "58ef9d675da4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "products",
        "currency",
        existing_type=postgresql.ENUM("Сом", "USD", name="Currency choices"),
        type_=sa.String(length=3),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "products",
        "currency",
        existing_type=sa.String(length=3),
        type_=postgresql.ENUM("Сом", "USD", name="Currency choices"),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
