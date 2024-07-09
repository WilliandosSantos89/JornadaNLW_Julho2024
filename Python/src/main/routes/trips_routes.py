from flask import jsonify, Blueprint

trips_routs_bp = Blueprint("trip_routs", __name__)

@trips_routs_bp.route("/trips", methods=["POST"])
def create_trip():
    return jsonify({"olá": "mundo"}), 200