from flask import Blueprint, jsonify

yardage_bp = Blueprint('yardage', __name__)

@yardage_bp.route('/api/yardage')
def get_yardage():
    return jsonify({
        "hole": 1,
        "yardage": 150,
        "location": {"lat": 40.1234, "lon": -86.1234}
    })




