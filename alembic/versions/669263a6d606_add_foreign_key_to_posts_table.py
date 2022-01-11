"""add foreign key to posts table

Revision ID: 669263a6d606
Revises: 3b04c15bfc95
Create Date: 2022-01-11 09:49:12.899958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '669263a6d606'
down_revision = '3b04c15bfc95'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE"
                          )
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
