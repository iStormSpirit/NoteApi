"""user add photo

Revision ID: 5450d6d72d65
Revises: c9d38cf75e50
Create Date: 2021-09-20 20:26:46.219875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5450d6d72d65'
down_revision = 'c9d38cf75e50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_file_model')),
    sa.UniqueConstraint('url', name=op.f('uq_file_model_url'))
    )
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_tag_name'), ['name'])

    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo_id', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint(batch_op.f('uq_user_model_username'), ['username'])
        batch_op.create_foreign_key(batch_op.f('fk_user_model_photo_id_file_model'), 'file_model', ['photo_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_user_model_photo_id_file_model'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('uq_user_model_username'), type_='unique')
        batch_op.drop_column('photo_id')

    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_tag_name'), type_='unique')

    op.drop_table('file_model')
    # ### end Alembic commands ###
