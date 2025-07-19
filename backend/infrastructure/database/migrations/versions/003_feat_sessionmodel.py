"""feat SessionModel; update UserModel(del location)

Revision ID: cd7de57d8a1c
Revises: c8a3f91411c3
Create Date: 2025-07-19 14:03:50.992988

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'cd7de57d8a1c'
down_revision: Union[str, None] = 'c8a3f91411c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('sessions',
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=False),
    sa.Column('ip', sa.String(), nullable=False),
    sa.Column('agent', sa.String(), nullable=False),
    sa.Column('revoked', sa.Boolean(), nullable=False),
    sa.Column('expired_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_sessions_refresh_token', 'sessions', ['refresh_token'], unique=True)

    op.drop_column('users', 'location')


def downgrade() -> None:
    op.add_column('users', sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_sessions_refresh_token'), table_name='sessions')
    op.drop_table('sessions')
