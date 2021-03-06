"""empty message

Revision ID: 7a51a649d6f9
Revises: 3f55d9c10c62
Create Date: 2017-04-13 22:45:21.781813

"""

# revision identifiers, used by Alembic.
revision = '7a51a649d6f9'
down_revision = '3f55d9c10c62'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apicache_allianceinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('allianceName', sa.String(length=100), nullable=True),
    sa.Column('dateFounded', sa.DateTime(), nullable=True),
    sa.Column('executorCorpID', sa.Integer(), nullable=True),
    sa.Column('ticker', sa.String(length=10), nullable=True),
    sa.Column('expire', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apicache_allianceinfo_allianceName'), 'apicache_allianceinfo', ['allianceName'], unique=False)
    op.create_index(op.f('ix_apicache_allianceinfo_executorCorpID'), 'apicache_allianceinfo', ['executorCorpID'], unique=False)
    op.drop_table('apicache_characterid')
    op.add_column('apicache_characterinfo', sa.Column('characterBirthday', sa.DateTime(), nullable=False))
    op.add_column('apicache_characterinfo', sa.Column('raceID', sa.Integer(), nullable=True))
    op.drop_column('apicache_characterinfo', 'corporationName')
    op.add_column('apicache_corporationinfo', sa.Column('ceoID', sa.Integer(), nullable=True))
    op.add_column('apicache_corporationinfo', sa.Column('creationDate', sa.DateTime(), nullable=True))
    op.add_column('apicache_corporationinfo', sa.Column('creatorID', sa.Integer(), nullable=True))
    op.add_column('apicache_corporationinfo', sa.Column('description', mysql.LONGTEXT(), nullable=True))
    op.add_column('apicache_corporationinfo', sa.Column('memberCount', sa.Integer(), nullable=True))
    op.add_column('apicache_corporationinfo', sa.Column('taxRate', sa.Float(), nullable=True))
    op.add_column('apicache_corporationinfo', sa.Column('ticker', sa.String(length=10), nullable=True))
    op.add_column('apicache_corporationinfo', sa.Column('url', sa.String(length=500), nullable=True))
    op.drop_index('ix_apicache_corporationinfo_allianceName', table_name='apicache_corporationinfo')
    op.drop_column('apicache_corporationinfo', 'allianceName')
    op.drop_column('roles', 'is_restrictive')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('is_restrictive', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('apicache_corporationinfo', sa.Column('allianceName', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True))
    op.create_index('ix_apicache_corporationinfo_allianceName', 'apicache_corporationinfo', ['allianceName'], unique=False)
    op.drop_column('apicache_corporationinfo', 'url')
    op.drop_column('apicache_corporationinfo', 'ticker')
    op.drop_column('apicache_corporationinfo', 'taxRate')
    op.drop_column('apicache_corporationinfo', 'memberCount')
    op.drop_column('apicache_corporationinfo', 'description')
    op.drop_column('apicache_corporationinfo', 'creatorID')
    op.drop_column('apicache_corporationinfo', 'creationDate')
    op.drop_column('apicache_corporationinfo', 'ceoID')
    op.add_column('apicache_characterinfo', sa.Column('corporationName', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True))
    op.drop_column('apicache_characterinfo', 'raceID')
    op.drop_column('apicache_characterinfo', 'characterBirthday')
    op.create_table('apicache_characterid',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_apicache_allianceinfo_executorCorpID'), table_name='apicache_allianceinfo')
    op.drop_index(op.f('ix_apicache_allianceinfo_allianceName'), table_name='apicache_allianceinfo')
    op.drop_table('apicache_allianceinfo')
    # ### end Alembic commands ###
