"""update initial data

Revision ID: bf536fadf8bf
Revises: 53dee3f829ad
Create Date: 2023-04-24 03:36:29.599601

"""
from alembic import op
import sqlalchemy as sa
from db_models import User


# revision identifiers, used by Alembic.
revision = 'bf536fadf8bf'
down_revision = '53dee3f829ad'
branch_labels = None
depends_on = None


def populate_data():
    data = [
        {'username': 'admin', 'password': 'apass', 'is_admin': True},
        {'username': 'client1', 'password': '1pass', 'is_admin': False},
        {'username': 'client2', 'password': '2pass', 'is_admin': False},
    ]
    for user_data in data:
        op.execute(f"UPDATE user SET is_admin = {user_data['is_admin']} WHERE username = '{user_data['username']}'")
        
def upgrade():
    populate_data()
        

def downgrade():
    pass