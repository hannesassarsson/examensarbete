from flask import Blueprint, request, jsonify

api_blueprint = Blueprint('api', __name__)

# Dummy endpoint för incheckning
@api_blueprint.route("/checkin", methods=["POST"])
def check_in():
    data = request.get_json()
    user_id = data.get("user_id")
    
    if not user_id:
        return jsonify({"error": "User ID saknas"}), 400
    
    # Här lägger vi senare in logik för att spara till databasen
    return jsonify({"message": f"Användare {user_id} incheckad"}), 200


# Dummy endpoint för utcheckning
@api_blueprint.route("/checkout", methods=["POST"])
def check_out():
    data = request.get_json()
    user_id = data.get("user_id")
    
    if not user_id:
        return jsonify({"error": "User ID saknas"}), 400
    
    # Här lägger vi senare in logik för att spara till databasen
    return jsonify({"message": f"Användare {user_id} utcheckad"}), 200