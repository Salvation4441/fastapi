"""auto-votes

Revision ID: 63e04071b5fa
Revises: ab7ed859f8eb
Create Date: 2022-09-07 15:13:31.879320

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '63e04071b5fa'
down_revision = 'ab7ed859f8eb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'votes',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'post_id')
    )


pass


def downgrade():
    op.drop_table('votes')


pass
