"""Initial schema

Revision ID: 18fab49636b9
Revises: 
Create Date: 2024-05-10 12:39:25.858623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18fab49636b9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('apiKey', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('userId'),
    sa.UniqueConstraint('apiKey')
    )
    op.create_index(op.f('ix_users_userId'), 'users', ['userId'], unique=False)
    op.create_table('posts',
    sa.Column('postId', sa.Integer(), nullable=False),
    sa.Column('authorId', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['authorId'], ['users.userId'], ),
    sa.PrimaryKeyConstraint('postId')
    )
    op.create_index(op.f('ix_posts_postId'), 'posts', ['postId'], unique=False)
    op.create_table('feedback',
    sa.Column('feedbackId', sa.Integer(), nullable=False),
    sa.Column('postId', sa.Integer(), nullable=True),
    sa.Column('positive', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['postId'], ['posts.postId'], ),
    sa.PrimaryKeyConstraint('feedbackId')
    )
    op.create_index(op.f('ix_feedback_feedbackId'), 'feedback', ['feedbackId'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_feedback_feedbackId'), table_name='feedback')
    op.drop_table('feedback')
    op.drop_index(op.f('ix_posts_postId'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_users_userId'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###