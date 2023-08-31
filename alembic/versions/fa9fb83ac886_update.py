"""update

Revision ID: fa9fb83ac886
Revises: 903762c944ff
Create Date: 2023-08-30 21:25:56.426753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa9fb83ac886'
down_revision: Union[str, None] = '903762c944ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
