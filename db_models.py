from server import db
from datetime import datetime
from enum import Enum
import uuid

class ImageDataStatus(Enum):
    APPROVED = 'approved'
    DECLINED = 'declined'
    PENDING = 'pending'


class ImageData(db.Model):
    name = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    ext = db.Column(db.String(20))
    result = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    status = db.Column(db.Enum(ImageDataStatus), default=ImageDataStatus.PENDING)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"ImageData(name='{self.name}' ext='{self.ext}' user_id='{self.user_id}' result='{self.result}' status='{self.status}' created_at='{self.created_at}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    is_admin = db.Column(db.Boolean, default=False)
    images = db.relationship('ImageData', backref = 'user', lazy = True)

    def __repr__(self):
        return f"User(id='{self.id}' username='{self.username}' password='{self.password}' is_admin='{self.is_admin}')"


