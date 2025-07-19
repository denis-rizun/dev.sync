"""feat UserModel

Revision ID: c8a3f91411c3
Revises: 5c7b5713b6d5
Create Date: 2025-07-18 21:53:19.245639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'c8a3f91411c3'
down_revision: Union[str, None] = '5c7b5713b6d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('mail', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('avatar', sa.String(), nullable=False, default="https://i.imgur.com/NTknVfT.jpeg"),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mail'),
    sa.UniqueConstraint('username')
    )


def downgrade() -> None:
    op.drop_table('users')
