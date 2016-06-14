"""empty message

Revision ID: d84f976530e1
Revises: 00ea66754d06
Create Date: 2016-06-14 10:33:50.685000

"""

# revision identifiers, used by Alembic.
revision = 'd84f976530e1'
down_revision = '00ea66754d06'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('organizer_name', sa.String()))
    op.add_column('events', sa.Column('organizer_description', sa.String()))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'organizer_name')
    op.drop_column('events', 'organizer_description')
    ### end Alembic commands ###
