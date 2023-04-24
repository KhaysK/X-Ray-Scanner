from functools import wraps
from flask import request, jsonify, g

def login_form_validator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        print(f"login_form_validator: {username=} {password=}")
        if not username:
            return jsonify({'error': 'username is required'}), 400
        if not password:
            return jsonify({'error': 'password is required'}), 400
        return f(username, password)
    return wrapper


def register_form_validator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        confirmPassword = request.json.get('confirmPassword', None)
        print(f"register_form_validator: {username=} {password=} {confirmPassword=}")
        if not username:
            return jsonify({'error': 'username is required'}), 400
        if not password:
            return jsonify({'error': 'password is required'}), 400
        if not confirmPassword:
            return jsonify({'error': 'confirmPassword field is required'}), 400
        if password != confirmPassword:
            return jsonify({'error': 'Passwords do not match'}), 400
        return f(username, password, confirmPassword)
    return wrapper



def update_image_validator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        image_name = request.json.get('image_name', None)
        image_status = request.json.get('image_status', None)
        print(f"update_image_validator: {image_name=} {image_status=}")
        if not image_name:
            return jsonify({'error': 'image_name is required'}), 400
        if not image_status:
            return jsonify({'error': 'image_status is required'}), 400
        return f(image_name, image_status)
    return wrapper


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if g.user is None:
            response = {'error': "You are not logged in"}
            return jsonify(response), 401
        return f(*args, **kwargs)
    return wrapper


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not g.user.is_admin:
            response = {'error': "You are not allowed"}
            return jsonify(response), 403
        return f(*args, **kwargs)
    return wrapper


def logout_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if g.user is not None:
            response = {'error': "You are logged in"}
            return jsonify(response), 409
        return f(*args, **kwargs)
    return wrapper