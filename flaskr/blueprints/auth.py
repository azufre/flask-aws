from datetime import datetime, timedelta

import jwt
from flask import Blueprint, current_app, jsonify, make_response, request
from werkzeug.security import check_password_hash, generate_password_hash

from ..models.Base import db
from ..models.User import User

bp = Blueprint('auth', __name__)


@bp.route('/auth/login', methods=['POST'])
def login():

    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return make_response(jsonify({
            'status': 'could not veify'
        }), 401)

    user = User.query.filter_by(email=data.get('email')).first()

    if not user:
        return make_response(jsonify({
            'status': 'could not veify'
        }), 401)

    if not check_password_hash(user.password, data.get('password')):
        print("No pasos")
        return make_response(jsonify({
            'status': 'could not veify'
        }), 401)

    token = jwt.encode({
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(minutes=60)
    }, current_app.config['SECRET_KEY'])

    return make_response(jsonify({
        'token': token.decode('UTF-8')
    }), 201)

@bp.route('/auth/signup', methods=['POST'])
def signup():

    data = request.get_json()

    if not data or\
        not data.get('email') or\
        not data.get('password') or\
        not data.get('name'):
        return make_response(jsonify({'status': 'could not create account'}), 401)
    
    user = User.query.filter_by(email=data.get('email')).first()

    if user:
        return make_response(jsonify({'status': 'User already exists. Please login'}), 202)

    user = User(
        name=data.get('name'),
        email=data.get('email'),
        password=generate_password_hash(data.get('password')),
    )

    db.session.add(user)
    db.session.commit()

    return make_response(jsonify({'status': 'Successfully registered.'}), 201)

