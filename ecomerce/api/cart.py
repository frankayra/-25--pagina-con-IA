from flask import Blueprint, jsonify, session
from database.models import Cart

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['GET'])
def view_cart():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401
    cart = Cart.query.filter_by(user_id=user_id).all()
    return jsonify([item.to_dict() for item in cart]), 200
