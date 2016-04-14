"""empty message

Revision ID: a92a35286d58
Revises: 9c3d75ef22cb
Create Date: 2016-04-14 20:48:59.408000

"""

# revision identifiers, used by Alembic.
revision = 'a92a35286d58'
down_revision = '9c3d75ef22cb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('waitlist_groups', sa.Column('constellationID', sa.Integer(), nullable=True))
    op.add_column('waitlist_groups', sa.Column('dockupID', sa.Integer(), nullable=True))
    op.add_column('waitlist_groups', sa.Column('enabled', sa.Boolean(), nullable=False))
    op.add_column('waitlist_groups', sa.Column('fcID', sa.Integer(), nullable=True))
    op.add_column('waitlist_groups', sa.Column('managerID', sa.Integer(), nullable=True))
    op.add_column('waitlist_groups', sa.Column('odering', sa.Integer(), nullable=False))
    op.add_column('waitlist_groups', sa.Column('status', sa.String(length=1000), nullable=True))
    op.add_column('waitlist_groups', sa.Column('systemID', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'waitlist_groups', 'constellation', ['constellationID'], ['constellationID'])
    op.create_foreign_key(None, 'waitlist_groups', 'solarsystem', ['systemID'], ['solarSystemID'])
    op.create_foreign_key(None, 'waitlist_groups', 'accounts', ['managerID'], ['id'])
    op.create_foreign_key(None, 'waitlist_groups', 'characters', ['fcID'], ['id'])
    op.create_foreign_key(None, 'waitlist_groups', 'station', ['dockupID'], ['stationID'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'waitlist_groups', type_='foreignkey')
    op.drop_constraint(None, 'waitlist_groups', type_='foreignkey')
    op.drop_constraint(None, 'waitlist_groups', type_='foreignkey')
    op.drop_constraint(None, 'waitlist_groups', type_='foreignkey')
    op.drop_constraint(None, 'waitlist_groups', type_='foreignkey')
    op.drop_column('waitlist_groups', 'systemID')
    op.drop_column('waitlist_groups', 'status')
    op.drop_column('waitlist_groups', 'odering')
    op.drop_column('waitlist_groups', 'managerID')
    op.drop_column('waitlist_groups', 'fcID')
    op.drop_column('waitlist_groups', 'enabled')
    op.drop_column('waitlist_groups', 'dockupID')
    op.drop_column('waitlist_groups', 'constellationID')
    ### end Alembic commands ###
