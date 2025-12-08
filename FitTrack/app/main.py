from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to FitTrack"}), 200


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/steps", methods=["POST"])
def record_steps():
    data = request.get_json() or {}
    steps = data.get("steps")
    if steps is None:
        return jsonify({"error": "missing 'steps' field"}), 400
    try:
        steps = int(steps)
    except (ValueError, TypeError):
        return jsonify({"error": "'steps' must be an integer"}), 400
    # In this minimal app we don't persist; just echo back
    return jsonify({"recorded": steps}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
