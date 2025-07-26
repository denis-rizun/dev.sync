"""feat ServerStatusEnum, WebhookSourceEnum, HistoryTriggerEnum;

Revision ID: ab37j3dk932j
Revises: cd64b851179c
Create Date: 2025-07-20 12:23:44.396155

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = 'ab37j3dk932j'
down_revision: Union[str, None] = 'cd64b851179c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    status_enum = postgresql.ENUM(
        'SUCCESS',
        'IN_PROGRESS',
        'ERROR',
        'WAITING',
        'EXCEPT',
        name='statusenum'
    )
    status_enum.create(op.get_bind(), checkfirst=True)
    source_enum = postgresql.ENUM('GITHUB', 'GITLAB', name='webhooksourceenum')
    source_enum.create(op.get_bind(), checkfirst=True)


def downgrade() -> None:
    status_enum = postgresql.ENUM(name='statusenum')
    status_enum.drop(op.get_bind(), checkfirst=True)
    source_enum = postgresql.ENUM(name='webhooksourceenum')
    source_enum.drop(op.get_bind(), checkfirst=True)
