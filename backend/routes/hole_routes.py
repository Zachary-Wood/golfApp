from flask import Blueprint, jsonify, request
from models.course import Course
from models.hole import Hole
from extensions import db
from geopy.distance import geodesic

hole_bp = Blueprint('hole', __name__)


@hole_bp.route('/api/course/<int:course_id>/holes', methods=['GET'])
def get_holes(course_id):
    course = Course.query.get_or_404(course_id)
    holes = [hole.to_dict() for hole in course.holes]
    return jsonify(holes)


@hole_bp.route('/api/hole/<int:hole_id>', methods=['GET'])
def get_hole(hole_id):
    hole = Hole.query.get_or_404(hole_id)
    return jsonify(hole.to_dict())


@hole_bp.route('/api/location', methods=['GET'])
def get_location():
   
    return jsonify({
        "lat": 41.2235,
        "lon": -85.8750
    })


@hole_bp.route('/api/hole/<int:hole_id>/distance', methods=['POST'])
def get_distance_to_green(hole_id):
    data = request.get_json()
    user_lat = data.get('lat')
    user_lon = data.get('lon')

    if not user_lat or not user_lon:
        return jsonify({"error": "Latitude and longitude required"}), 400

    hole = Hole.query.get_or_404(hole_id)

    green_coords = (hole.green_lat, hole.green_lon)
    user_coords = (user_lat, user_lon)

    distance = geodesic(user_coords, green_coords).yards

    return jsonify({
        "hole": hole.number,
        "distance_to_green_yards": round(distance, 1)
    })
