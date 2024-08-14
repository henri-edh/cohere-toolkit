"""Add model and deployment to Agents

Revision ID: 3f207ae41477
Revises: 922e874930bf
Create Date: 2024-06-15 23:02:22.350756

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "3f207ae41477"
down_revision: Union[str, None] = "922e874930bf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "agents",
        "model",
        existing_type=sa.VARCHAR(length=14),
        type_=sa.Text(),
        existing_nullable=False,
    )
    op.alter_column(
        "agents",
        "deployment",
        existing_type=sa.VARCHAR(length=15),
        type_=sa.Text(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "agents",
        "deployment",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(length=15),
        existing_nullable=False,
    )
    op.alter_column(
        "agents",
        "model",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(length=14),
        existing_nullable=False,
    )
    # ### end Alembic commands ###