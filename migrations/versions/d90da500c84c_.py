"""empty message

Revision ID: d90da500c84c
Revises: 565cb2af7fa3
Create Date: 2016-04-14 14:01:43.678000

"""

# revision identifiers, used by Alembic.
revision = 'd90da500c84c'
down_revision = '565cb2af7fa3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fittings', sa.Column('created', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fittings', 'created')
    ### end Alembic commands ###
