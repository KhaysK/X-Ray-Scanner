"""create initial data

Revision ID: e4a922f19886
Revises: 31b0b281778b
Create Date: 2023-04-24 23:08:01.286558

"""
from alembic import op
import sqlalchemy as sa
from db_models import User

# revision identifiers, used by Alembic.
revision = 'e4a922f19886'
down_revision = '31b0b281778b'
branch_labels = None
depends_on = None

def populate_data():
    data = [
        {'username': 'admin', 'password': 'apass', 'is_admin': True},
        {'username': 'bdmin', 'password': 'bpass', 'is_admin': True},
        {'username': 'client1', 'password': '1pass', 'is_admin': False},
        {'username': 'client2', 'password': '2pass', 'is_admin': False},
    ]
    op.bulk_insert(User.__table__, data)


def upgrade():
    populate_data()


def downgrade():
    pass
