"""empty message

Revision ID: aca3c4b65e26
Revises: 107743f414c2
Create Date: 2016-02-17 14:10:11.178675

"""

# revision identifiers, used by Alembic.
revision = 'aca3c4b65e26'
down_revision = '107743f414c2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('location', sa.String(), nullable=True))
    op.add_column('job', sa.Column('perks', sa.String(), nullable=True))
    op.add_column('job', sa.Column('salary', sa.Integer(), nullable=True))
    op.add_column('job', sa.Column('summary', sa.String(), nullable=True))
    op.add_column('person', sa.Column('email', sa.String(length=120), nullable=True))
    op.add_column('person', sa.Column('job_title', sa.String(length=100), nullable=True))
    op.add_column('person', sa.Column('location', sa.String(length=100), nullable=True))
    op.add_column('person', sa.Column('summary', sa.String(), nullable=True))
    op.add_column('person', sa.Column('website', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'person', ['email'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_column('person', 'website')
    op.drop_column('person', 'summary')
    op.drop_column('person', 'location')
    op.drop_column('person', 'job_title')
    op.drop_column('person', 'email')
    op.drop_column('job', 'summary')
    op.drop_column('job', 'salary')
    op.drop_column('job', 'perks')
    op.drop_column('job', 'location')
    ### end Alembic commands ###
