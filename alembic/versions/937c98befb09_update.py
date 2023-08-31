"""update

Revision ID: 937c98befb09
Revises: 7151c595a295
Create Date: 2023-08-31 12:55:08.569938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '937c98befb09'
down_revision: Union[str, None] = '7151c595a295'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
