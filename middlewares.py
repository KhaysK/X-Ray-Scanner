from functools import wraps
from flask import request, jsonify, g

def login_form_validator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        print(f"login_form_validator: {username=} {password=}")
        if not username:
            return jsonify({'error': 'Username is required'}), 400
        if not password:
            return jsonify({'error': 'Password is required'}), 400
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
            return jsonify({'error': 'Username is required'}), 400
        if not password:
            return jsonify({'error': 'Password is required'}), 400
        if not confirmPassword:
            return jsonify({'error': 'Confirm password field is required'}), 400
        if password != confirmPassword:
            return jsonify({'error': 'Passwords do not match'}), 400
        return f(username, password, confirmPassword)
    return wrapper


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if g.user is None:
            response = {'error': "You are not logged in"}
            return jsonify(response), 401
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