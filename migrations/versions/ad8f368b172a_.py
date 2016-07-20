"""

Revision ID: ad8f368b172a
Revises: af578c9d3d7e
Create Date: 2016-07-20 18:37:09.510216

"""

# revision identifiers, used by Alembic.
revision = 'ad8f368b172a'
down_revision = 'af578c9d3d7e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proposal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('potential_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('potential_venue', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_proposal_potential_venue_venue'), 'venue', ['potential_venue'], ['id'])

    with op.batch_alter_table('proposal_version', schema=None) as batch_op:
        batch_op.add_column(sa.Column('potential_time', sa.DateTime(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('potential_venue', sa.Integer(), autoincrement=False, nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proposal_version', schema=None) as batch_op:
        batch_op.drop_column('potential_venue')
        batch_op.drop_column('potential_time')

    with op.batch_alter_table('proposal', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_proposal_potential_venue_venue'), type_='foreignkey')
        batch_op.drop_column('potential_venue')
        batch_op.drop_column('potential_time')

    ### end Alembic commands ###
