"""role

Revision ID: 2512efb0cf5c
Revises: 28c08d3af2e4
Create Date: 2021-09-08 22:09:33.608099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2512efb0cf5c'
down_revision = '28c08d3af2e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_model', sa.Column('role', sa.String(length=32), server_default='admin', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_model', 'role')
    # ### end Alembic commands ###
