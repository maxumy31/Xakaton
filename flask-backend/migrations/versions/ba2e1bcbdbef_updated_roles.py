"""Updated roles

Revision ID: ba2e1bcbdbef
Revises: 6d3fdfc911fb
Create Date: 2024-04-27 23:44:40.504063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba2e1bcbdbef'
down_revision = '6d3fdfc911fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_column('form_access')
        batch_op.drop_column('admin_panel')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_panel', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('form_access', sa.BOOLEAN(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
