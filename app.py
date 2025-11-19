# app.py
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory "database"
# Keys are integer user ids, values are dicts with user info
users = {}
next_id = 1

def make_user_response(user_id, data):
    return {"id": user_id, **data}

@app.route("/users", methods=["GET"])
def list_users():
    """Return list of all users."""
    return jsonify([make_user_response(uid, data) for uid, data in users.items()]), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Return a single user by id."""
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(make_user_response(user_id, user)), 200

@app.route("/users", methods=["POST"])
def create_user():
    """Create a new user.
    Expected JSON body: { "name": "Alice", "email": "alice@example.com" }
    """
    global next_id
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    payload = request.get_json()
    name = payload.get("name")
    email = payload.get("email")
    if not name or not email:
        return jsonify({"error": "Missing 'name' or 'email'"}), 400

    user_id = next_id
    users[user_id] = {"name": name, "email": email}
    next_id += 1
    return jsonify(make_user_response(user_id, users[user_id])), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update an existing user. JSON body may contain 'name' and/or 'email'."""
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    payload = request.get_json()
    name = payload.get("name")
    email = payload.get("email")
    if name:
        users[user_id]["name"] = name
    if email:
        users[user_id]["email"] = email

    return jsonify(make_user_response(user_id, users[user_id])), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a user by id."""
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(user_id)
    return jsonify({"deleted": make_user_response(user_id, deleted)}), 200

@app.route("/")
def index():
    return (
        "User API — endpoints: GET /users, GET /users/<id>, POST /users, PUT /users/<id>, DELETE /users/<id>"
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
