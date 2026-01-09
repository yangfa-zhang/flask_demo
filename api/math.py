from flask import Blueprint, request, jsonify

math_bp = Blueprint("math", __name__, url_prefix="/api/math")

# @math_bp.route("/square", methods=["GET","POST"])
@math_bp.route("/square", methods=["POST"])
def square():
    """
    输入一个数字，返回它的平方
    """
    # 1️⃣ GET: /api/math/square?n=3
    if request.method == "GET":
        n = request.args.get("n")

    # 2️⃣ POST: curl -X POST http://局域网ip/api/math/square -H "Content-Type: application/json" -d '{"n": 8}'
    else:
        data = request.get_json(silent=True) or {}
        n = data.get("n")

    # 参数校验
    if n is None:
        return jsonify({"error": "missing parameter n"}), 400

    try:
        n = float(n)
    except ValueError:
        return jsonify({"error": "n must be a number"}), 400

    return jsonify({
        "input": n,
        "square": n * n
    })
