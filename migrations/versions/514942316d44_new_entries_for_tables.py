"""new entries for tables

Revision ID: 514942316d44
Revises: 
Create Date: 2023-09-03 14:44:05.438222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '514942316d44'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brand_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'brands', ['brand_id'], ['id'])
        batch_op.create_foreign_key(None, 'categories', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category_id')
        batch_op.drop_column('brand_id')

    # ### end Alembic commands ###
