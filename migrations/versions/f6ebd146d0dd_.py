"""empty message

Revision ID: f6ebd146d0dd
Revises: 8113af5e2643
Create Date: 2016-05-18 11:27:55.490215

"""

# revision identifiers, used by Alembic.
revision = 'f6ebd146d0dd'
down_revision = '8113af5e2643'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('access_token', sa.String(length=128), nullable=True))
    op.add_column('accounts', sa.Column('access_token_expires', sa.DateTime(), nullable=True))
    op.add_column('accounts', sa.Column('refresh_token', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accounts', 'refresh_token')
    op.drop_column('accounts', 'access_token_expires')
    op.drop_column('accounts', 'access_token')
    ### end Alembic commands ###
