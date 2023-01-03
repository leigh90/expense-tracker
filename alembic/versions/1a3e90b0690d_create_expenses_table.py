"""create expenses table

Revision ID: 1a3e90b0690d
Revises: 
Create Date: 2023-01-03 16:25:35.415588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a3e90b0690d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'expenses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('amount_spent', sa.Integer, nullable=False),
        sa.Column('payee', sa.String(200), nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('time', sa.Time, nullable=False),
        sa.Column('transaction_cost', sa.Integer, nullable=True),
        sa.Column('category', sa.String(120), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("expenses")
