"""create posts table

Revision ID: 31a46396ed7d
Revises: 
Create Date: 2022-01-09 18:25:05.977333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31a46396ed7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
