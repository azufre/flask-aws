from flask import Blueprint, jsonify

bp  = Blueprint('home', __name__)

@bp.route('/')
def index():
    return jsonify({
        'status': 'running'
    })