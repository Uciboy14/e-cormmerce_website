"""upgrade

Revision ID: 1e2064f5671d
Revises: fa9fb83ac886
Create Date: 2023-08-30 21:36:01.899404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e2064f5671d'
down_revision: Union[str, None] = 'fa9fb83ac886'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
