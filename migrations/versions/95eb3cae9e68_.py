"""empty message

Revision ID: 95eb3cae9e68
Revises: aacfc1555e57
Create Date: 2016-12-30 20:43:41.455000

"""

# revision identifiers, used by Alembic.
revision = '95eb3cae9e68'
down_revision = 'aacfc1555e57'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role_history',
    sa.Column('entryID', sa.Integer(), nullable=False),
    sa.Column('accountID', sa.Integer(), nullable=False),
    sa.Column('byAccountID', sa.Integer(), nullable=False),
    sa.Column('note', mysql.TEXT(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['accountID'], ['accounts.id'], ),
    sa.ForeignKeyConstraint(['byAccountID'], ['accounts.id'], ),
    sa.PrimaryKeyConstraint('entryID')
    )
    op.create_index(op.f('ix_role_history_time'), 'role_history', ['time'], unique=False)

    op.create_table('role_changes',
    sa.Column('roleChangeID', sa.Integer(), nullable=False),
    sa.Column('entryID', sa.Integer(), nullable=False),
    sa.Column('roleID', sa.Integer(), nullable=False),
    sa.Column('added', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['entryID'], ['role_history.entryID'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['roleID'], ['roles.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('roleChangeID')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ##
    op.drop_table('role_changes')
    op.drop_index(op.f('ix_role_history_time'), table_name='role_history')
    op.drop_table('role_history')

    ### end Alembic commands ###
