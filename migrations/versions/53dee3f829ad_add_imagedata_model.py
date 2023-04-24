"""add ImageData model

Revision ID: 53dee3f829ad
Revises: aa43d5958fe2
Create Date: 2023-04-24 00:49:57.416854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53dee3f829ad'
down_revision = 'aa43d5958fe2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_data',
    sa.Column('name', sa.String(length=36), nullable=False),
    sa.Column('ext', sa.String(length=20), nullable=True),
    sa.Column('result', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('name')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    op.drop_table('image_data')
    # ### end Alembic commands ###
