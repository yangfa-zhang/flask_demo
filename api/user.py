from flask import Blueprint, request, jsonify

user_bp = Blueprint("user", __name__, url_prefix="/api/user")


@user_bp.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "world")
    return jsonify({
        "msg": f"hello {name}"
    })


@user_bp.route("/add", methods=["POST"])
def add_user():
    data = request.get_json()
    return jsonify({
        "status": "ok",
        "data": data
    })
