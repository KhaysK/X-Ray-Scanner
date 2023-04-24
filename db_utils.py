from db_models import User, ImageData, ImageDataStatus
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


def get_image_data_statuses():
    return [status.value for status in ImageDataStatus]

def get_image_data_status(status: str):
    try:
        image_data_status = ImageDataStatus(status)
        return image_data_status
    except ValueError:
        return None


def update_image_data_status(image_data: ImageData, image_status: ImageDataStatus):
    image_data.status = image_status
    db.session.commit()

def get_image_data(image_name: str):
    return ImageData.query.get(image_name)

def get_image_datas():
    return ImageData.query.order_by(ImageData.created_at.desc()).all()

def get_user_image_datas(user:User):
    return ImageData.query.order_by(ImageData.created_at.desc()).filter_by(user=user)

def create_image_data(name:str, ext:str, result:str, user_id = None):
    image_data = ImageData(name=name, ext=ext, result=result, user_id=user_id)
    db.session.add(image_data)
    db.session.commit()
    return image_data

def image_data_to_dict(image_data: ImageData):
    return {
        'name': image_data.name,
        'ext': image_data.ext,
        'result': image_data.result,
        'created_at': image_data.created_at,
        'status': image_data.status.value if image_data.status else None,
        'username': image_data.user.username if image_data.user else None
    }