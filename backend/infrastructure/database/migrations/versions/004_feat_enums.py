"""feat ServerStatusEnum;

Revision ID: e3a9c73a9af1
Revises: cd7de57d8a1c
Create Date: 2025-07-19 20:25:44.713621

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = 'e3a9c73a9af1'
down_revision: Union[str, None] = 'cd7de57d8a1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    server_status_enum = postgresql.ENUM('ACTIVE', 'INACTIVE', name='serverstatusenum')
    server_status_enum.create(op.get_bind(), checkfirst=True)


def downgrade() -> None:
    server_status_enum = postgresql.ENUM(name='serverstatusenum')
    server_status_enum.drop(op.get_bind(), checkfirst=True)
