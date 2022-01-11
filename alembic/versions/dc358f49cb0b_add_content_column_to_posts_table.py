"""add content column to posts table

Revision ID: dc358f49cb0b
Revises: 31a46396ed7d
Create Date: 2022-01-09 18:50:48.368312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc358f49cb0b'
down_revision = '31a46396ed7d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
