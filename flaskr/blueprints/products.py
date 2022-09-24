from flask import Blueprint, jsonify, request

from ..models.Base import db
from ..models.Product import Product
from ..decorators.auth import token_required

bp = Blueprint('products', __name__)

@bp.route('/products/create', methods=['POST'])
@token_required
def create_product(current_user):

    data = request.get_json()

    product = Product(
        name= data['name'],
        price= data['price']
    )

    db.session.add(product)

    db.session.commit()

    return jsonify(product.to_dict())

@bp.route('/products', methods=['GET'])
def get_list():
    products = db.session.execute(db.select(Product).order_by(Product.name)).all()
    return jsonify([product[0].to_dict() for product in products])

@bp.route('/products/<int:id>', methods=['GET'])
def get_by_id(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())

@bp.route('/products/<int:id>/delete', methods=['POST'])
def delete_by_id(id):
    product = Product.query.get_or_404(id)
    
    db.session.delete(product)
    db.session.commit()

    return jsonify(product.to_dict())