"""Added form table

Revision ID: fa1b40b911a9
Revises: ef05b0bea680
Create Date: 2024-04-20 20:44:33.695892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa1b40b911a9'
down_revision = 'ef05b0bea680'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('form',
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('info', sa.JSON(), nullable=True),
    sa.Column('university_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('role')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('form')
    # ### end Alembic commands ###
