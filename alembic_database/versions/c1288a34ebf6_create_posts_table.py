"""create posts table

Revision ID: c1288a34ebf6
Revises: 
Create Date: 2022-09-07 13:37:00.840675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1288a34ebf6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    #     id = Column(Integer, primary_key=True, nullable=False)
    #     title = Column(String, nullable=False)
    #     content = Column(String, nullable=False)
    #     published = Column(Boolean, server_default='True', nullable=False)
    #     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    #     owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    #     # its gives a relations between the user and post
    #     owner = relationship('User')
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False, unique=True),
        sa.Column('content', sa.String(), nullable=False),
        sa.Column('published', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
