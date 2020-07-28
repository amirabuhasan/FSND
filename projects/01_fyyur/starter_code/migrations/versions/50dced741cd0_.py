"""empty message

Revision ID: 50dced741cd0
Revises: 9baaf5d69406
Create Date: 2020-07-29 01:17:45.867192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50dced741cd0'
down_revision = '9baaf5d69406'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('artists', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'website')
    op.drop_table('shows')
    # ### end Alembic commands ###
