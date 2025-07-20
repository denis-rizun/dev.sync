"""feat WebhookModel

Revision ID: 6b8d78ca8f55
Revises: ab37j3dk932j
Create Date: 2025-07-20 12:25:44.396155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = '6b8d78ca8f55'
down_revision: Union[str, None] = 'ab37j3dk932j'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('webhooks',
    sa.Column(
        'status',
        postgresql.ENUM(
            'SUCCESS', 'IN_PROGRESS', 'ERROR', 'WAITING', 'EXCEPT',
            name='statusenum',
            create_type=False
        ),
        nullable=False,
        default='WAITING'
    ),
    sa.Column('repository', sa.String(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('branch', sa.String(), nullable=False),
    sa.Column('shell', sa.String(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('server_id', sa.UUID(), nullable=False),
    sa.Column(
        'server_status',
        postgresql.ENUM('ACTIVE', 'INACTIVE', name='serverstatusenum', create_type=False),
        nullable=False,
        default='ACTIVE'
    ),
    sa.Column(
        'source',
        postgresql.ENUM('GITHUB', 'GITLAB', name='webhooksourceenum', create_type=False),
        nullable=False,
    ),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('key'),
    sa.UniqueConstraint('repository')
    )


def downgrade() -> None:
    op.drop_table('webhooks')
