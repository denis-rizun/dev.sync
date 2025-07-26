"""feat ServerModel;

Revision ID: cd64b851179c
Revises: e3a9c73a9af1
Create Date: 2025-07-19 20:26:44.713621

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = 'cd64b851179c'
down_revision: Union[str, None] = 'e3a9c73a9af1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('servers',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column(
        'server_status',
        postgresql.ENUM('ACTIVE', 'INACTIVE', name='serverstatusenum', create_type=False),
        nullable=False,
        default='ACTIVE'
    ),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('ip', sa.String(), nullable=False),
    sa.Column('port', sa.Integer(), nullable=False),
    sa.Column('account', sa.String(), nullable=False),
    sa.Column('pkey', sa.String(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('servers')
