"""Add item column

Revision ID: 77b61697b1ae
Revises: 1a3e90b0690d
Create Date: 2023-01-04 15:29:41.548481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77b61697b1ae'
down_revision = '1a3e90b0690d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('expenses', sa.Column('item',sa.String))


def downgrade() -> None:
    op.drop_column('expenses', 'item')
