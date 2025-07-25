"""feat HistoryModel;

Revision ID: 7cdf5310f42d
Revises: 6b8d78ca8f55
Create Date: 2025-07-20 18:29:27.662736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = '7cdf5310f42d'
down_revision: Union[str, None] = '6b8d78ca8f55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('histories',
    sa.Column(
        'status',
        postgresql.ENUM(
            'SUCCESS',
            'IN_PROGRESS',
            'ERROR',
            'WAITING',
            'EXCEPT',
            name='statusenum',
            create_type=False
        ),
        nullable=False,
    ),
    sa.Column('output', sa.String(), nullable=False),
    sa.Column('pusher', sa.String(), nullable=True),
    sa.Column('webhook_id', sa.UUID(), nullable=False),
    sa.Column('server_id', sa.UUID(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.ForeignKeyConstraint(['webhook_id'], ['webhooks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('histories')
