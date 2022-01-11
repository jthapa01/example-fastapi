"""add last few columns to posts table

Revision ID: 705287e29268
Revises: 6232cf9c1127
Create Date: 2022-01-09 20:41:44.506828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '705287e29268'
down_revision = '6232cf9c1127'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
