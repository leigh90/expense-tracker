"""create category table

Revision ID: a70fed4d275d
Revises: 
Create Date: 2023-02-07 08:22:50.754392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a70fed4d275d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'category',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),

    )
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
    op.drop_table("category")
    op.drop_table("expenses")

