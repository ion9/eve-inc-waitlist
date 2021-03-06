"""empty message

Revision ID: 0c6c4b5461ce
Revises: 7b75d315ee36
Create Date: 2016-05-05 21:16:48.349000

"""

# revision identifiers, used by Alembic.
revision = '0c6c4b5461ce'
down_revision = '7b75d315ee36'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crest_fleets',
    sa.Column('fleetID', sa.BigInteger(), nullable=False),
    sa.Column('logiWingID', sa.BigInteger(), nullable=True),
    sa.Column('logiSquadID', sa.BigInteger(), nullable=True),
    sa.Column('sniperWingID', sa.BigInteger(), nullable=True),
    sa.Column('sniperSquadID', sa.BigInteger(), nullable=True),
    sa.Column('dpsWingID', sa.BigInteger(), nullable=True),
    sa.Column('dpsSquadID', sa.BigInteger(), nullable=True),
    sa.Column('otherWingID', sa.BigInteger(), nullable=True),
    sa.Column('otherSquadID', sa.BigInteger(), nullable=True),
    sa.Column('groupID', sa.Integer(), nullable=False),
    sa.Column('compID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['compID'], ['accounts.id'], ),
    sa.ForeignKeyConstraint(['groupID'], ['waitlist_groups.groupID'], ),
    sa.PrimaryKeyConstraint('fleetID')
    )
    op.create_table('send_invite',
    sa.Column('sendInviteID', sa.Integer(), nullable=False),
    sa.Column('characterID', sa.Integer(), nullable=True),
    sa.Column('fleetID', sa.BigInteger(), nullable=True),
    sa.Column('inviteCount', sa.Integer(), nullable=True),
    sa.Column('sendAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['characterID'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['fleetID'], ['crest_fleets.fleetID'], ),
    sa.PrimaryKeyConstraint('sendInviteID')
    )
    op.add_column(u'waitlist_entries', sa.Column('timeInvited', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'waitlist_entries', 'timeInvited')
    op.drop_table('send_invite')
    op.drop_table('crest_fleets')
    ### end Alembic commands ###
