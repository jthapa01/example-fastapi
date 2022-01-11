"""add content column to  posts table

Revision ID: a5a4daba03b5
Revises: 11b6ce9fec91
Create Date: 2022-01-11 09:45:22.016621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5a4daba03b5'
down_revision = '11b6ce9fec91'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
