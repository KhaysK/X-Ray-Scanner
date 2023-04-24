from flask import (
    Blueprint, request, g, session, jsonify
)

from middlewares import login_form_validator, register_form_validator, login_required, logout_required
from db_utils import get_user, get_user_by, get_user_by_username, create_user
from db_models import User
import os, uuid
import model

bp = Blueprint('routes', __name__, url_prefix='/api')

# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password
    
#     def __str__(self):
#         return f'User(id={self.id}, username={self.username}, password={self.password})'


# users = {
#     'admin_id'  : User(id='admin_id', username='admin', password='apass'),
#     'client1_id': User(id='client1_id', username='client1', password='1pass'),
#     'client2_id': User(id='client2_id', username='client2', password='2pass')
# }


def set_user(user: User):
    session.clear()
    session['user_id'] = user.id


@bp.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_user(user_id)
        print('load_logged_in_user:', g.user)


@bp.route('/getuser')
def getuser():
    response = {}
    if g.user is not None:
        response['username'] = g.user.username
    print(f'getuser: {response=}')
    return jsonify(response)



@bp.route('/logout')
@login_required
def logout():
    session.clear()
    response = {'message': "You have logged out sucessfully"}
    return jsonify(response)



@bp.route('/login', methods=['POST'])
@logout_required
@login_form_validator
def login(username, password):
    user = get_user_by(username, password)
    if user is None:
        response = {'error': 'Invalid username or password'}
        return jsonify(response), 401
    else:
        set_user(user)
        print('login:', user)
        response = {
            'username': user.username
        }
        return jsonify(response)


@bp.route('/register', methods=['POST'])
@logout_required
@register_form_validator
def register(username, password, confirmPassword):
    user = get_user_by_username(username)
    if user is not None:
        response = {'error': "Username is already taken"}
        return jsonify(response), 400
    else:
        user = create_user(username, password)
        set_user(user)
        print('register:', user)
        response = {
            'username': user.username
        }
        return jsonify(response)


@bp.route('/upload', methods=['POST'])
def upload_file():
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']


    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    allowed_extensions = ['.jpeg', '.png']

    file_extension = str(os.path.splitext(file.filename)[1])
    print(file_extension)
    if file_extension not in allowed_extensions:
        return jsonify({'error': f"File should have one of {allowed_extensions} extensions"}), 400

    filename = str(uuid.uuid4()) + file_extension

    
    filepath = os.path.join('imageStorage', filename)
    file.save(filepath)

    return jsonify({'result': model.get_prediction(filepath) })
