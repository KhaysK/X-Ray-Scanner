"""initial commit

Revision ID: 31b0b281778b
Revises: 
Create Date: 2023-04-24 23:07:16.218032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31b0b281778b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('image_data',
    sa.Column('name', sa.String(length=36), nullable=False),
    sa.Column('ext', sa.String(length=20), nullable=True),
    sa.Column('result', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('APPROVED', 'DECLINED', 'PENDING', name='imagedatastatus'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image_data')
    op.drop_table('user')
    # ### end Alembic commands ###