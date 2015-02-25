"""empty message

Revision ID: 47ab3cc6667a
Revises: 36b93d81ad60
Create Date: 2015-02-18 13:07:06.362823

"""

# revision identifiers, used by Alembic.
revision = '47ab3cc6667a'
down_revision = '36b93d81ad60'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loguser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Jan', sa.String(), nullable=False),
    sa.Column('Orlik', sa.String(), nullable=False),
    sa.Column('Muz', sa.Boolean(name='zena'), nullable=True),
    sa.Column('datum_insertu', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_loguser'),
    sqlite_autoincrement=True
    )
    op.create_index('ix_loguser_Orlik', 'loguser', ['Orlik'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_loguser_Orlik', table_name='loguser')
    op.drop_table('loguser')
    ### end Alembic commands ###
