"""create_main_tables
Revision ID: 76ec7d2226c1
Revises: 
Create Date: 2022-10-07 06:15:59.611962
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = '76ec7d2226c1'
down_revision = None
branch_labels = None
depends_on = None


def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )


def upgrade() -> None:
    create_cleanings_table()


def downgrade() -> None:
    pass