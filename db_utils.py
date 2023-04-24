from db_models import User, ImageData
from server import db


def get_user(user_id):
    return User.query.get(int(user_id))

def get_user_by(username: str, password: str):
    return User.query.filter_by(username=username, password=password).first()

def get_user_by_username(username: str):
    return User.query.filter_by(username=username).first()

def create_user(username: str, password: str, is_admin:bool = False):
    user = User(username=username, password=password, is_admin=is_admin)
    db.session.add(user)
    db.session.commit()
    return user


def get_image_datas():
    return ImageData.query.order_by(ImageData.created_at.desc()).all()

def get_user_image_datas(user:User):
    return ImageData.query.order_by(ImageData.created_at.desc()).filter_by(user=user)

def create_image_data(name:str, ext:str, result:str, user_id = None):
    image_data = ImageData(name=name, ext=ext, result=result, user_id=user_id)
    db.session.add(image_data)
    db.session.commit()
    return image_data

