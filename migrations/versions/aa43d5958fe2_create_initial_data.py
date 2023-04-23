"""create initial data

Revision ID: aa43d5958fe2
Revises: ab436f16cb5c
Create Date: 2023-04-23 18:57:55.246383

"""
from alembic import op
import sqlalchemy as sa
from db_models import User


# revision identifiers, used by Alembic.
revision = 'aa43d5958fe2'
down_revision = 'ab436f16cb5c'
branch_labels = None
depends_on = None


def populate_data():
    data = [
        {'username': 'admin', 'password': 'apass'},
        {'username': 'client1', 'password': '1pass'},
        {'username': 'client2', 'password': '2pass'},
    ]
    op.bulk_insert(User.__table__, data)


def upgrade():
    populate_data()
        

def downgrade():
    pass
