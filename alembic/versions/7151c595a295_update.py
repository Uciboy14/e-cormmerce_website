"""update

Revision ID: 7151c595a295
Revises: 1e2064f5671d
Create Date: 2023-08-31 05:24:17.978124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7151c595a295'
down_revision: Union[str, None] = '1e2064f5671d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
