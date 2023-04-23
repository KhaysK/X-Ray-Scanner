from db_models import User
from server import db


def get_user(user_id):
    return User.query.get(int(user_id))

def get_user_by(username: str, password: str):
    return User.query.filter_by(username=username, password=password).first()

def get_user_by_username(username: str):
    return User.query.filter_by(username=username).first()

def create_user(username: str, password: str):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user
