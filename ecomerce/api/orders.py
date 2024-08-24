from flask import Blueprint, jsonify, session
from database.models import Order

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['GET'])
def view_orders():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([order.to_dict() for order in orders]), 200
