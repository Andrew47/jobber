"""empty message

Revision ID: 76b12d078e4d
Revises: 415f6eedf7d4
Create Date: 2016-02-19 10:04:38.892529

"""

# revision identifiers, used by Alembic.
revision = '76b12d078e4d'
down_revision = '415f6eedf7d4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('photo', sa.String(length=250), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'photo')
    ### end Alembic commands ###
