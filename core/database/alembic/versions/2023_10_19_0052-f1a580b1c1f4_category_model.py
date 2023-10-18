"""Category Model

Revision ID: f1a580b1c1f4
Revises: a4c275968bed
Create Date: 2023-10-19 00:52:26.844875

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f1a580b1c1f4"
down_revision: Union[str, None] = "a4c275968bed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "categorys",
        sa.Column("title", sa.String(length=20), nullable=False),
        sa.Column("description", sa.String(length=100), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("categorys")
    # ### end Alembic commands ###
