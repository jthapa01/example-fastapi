"""add foreign-key to posts table

Revision ID: 6232cf9c1127
Revises: 53d1d913f93a
Create Date: 2022-01-09 20:11:13.919740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6232cf9c1127'
down_revision = '53d1d913f93a'
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
