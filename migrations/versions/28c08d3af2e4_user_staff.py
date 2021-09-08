"""user staff

Revision ID: 28c08d3af2e4
Revises: 8a984e86b17a
Create Date: 2021-09-08 21:01:53.100060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28c08d3af2e4'
down_revision = '8a984e86b17a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_model', sa.Column('is_staff', sa.Boolean(), server_default='true', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_model', 'is_staff')
    # ### end Alembic commands ###
