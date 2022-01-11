"""auto-vote

Revision ID: e2959d4cc7bd
Revises: 705287e29268
Create Date: 2022-01-10 20:41:18.592517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2959d4cc7bd'
down_revision = '705287e29268'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_constraint('post_users_fk', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('posts', 'owner_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('post_users_fk', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###
