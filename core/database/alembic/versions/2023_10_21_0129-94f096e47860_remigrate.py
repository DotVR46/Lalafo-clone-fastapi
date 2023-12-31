"""ReMigrate

Revision ID: 94f096e47860
Revises: 
Create Date: 2023-10-21 01:29:32.187571

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "94f096e47860"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "categories",
        sa.Column("title", sa.String(length=20), nullable=False),
        sa.Column("description", sa.String(length=100), nullable=False),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["parent_id"],
            ["categories.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("username", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(length=32), nullable=True),
        sa.Column("phone", sa.String(length=12), nullable=False),
        sa.Column("bio", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("phone"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "products",
        sa.Column("title", sa.String(length=60), nullable=False),
        sa.Column("description", sa.String(length=300), nullable=False),
        sa.Column("city", sa.String(length=20), nullable=False),
        sa.Column("price", sa.Numeric(precision=8, scale=0), nullable=False),
        sa.Column(
            "currency", sa.Enum("Сом", "USD", name="Currency choices"), nullable=False
        ),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["categories.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("products")
    op.drop_table("users")
    op.drop_table("categories")
    # ### end Alembic commands ###
