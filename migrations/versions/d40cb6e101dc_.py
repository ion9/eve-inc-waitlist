"""empty message

Revision ID: d40cb6e101dc
Revises: ea41446517f3
Create Date: 2016-03-29 20:43:23.952000

"""

# revision identifiers, used by Alembic.
revision = 'd40cb6e101dc'
down_revision = 'ea41446517f3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('cbs_level', sa.SmallInteger(), nullable=False))
    op.add_column('characters', sa.Column('lc_level', sa.SmallInteger(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('characters', 'lc_level')
    op.drop_column('characters', 'cbs_level')
    ### end Alembic commands ###
