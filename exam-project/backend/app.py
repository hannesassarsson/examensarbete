import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sqlite3
import jwt
from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import wraps
from datetime import datetime, timedelta
from database.db_manager import DatabaseManager
from google.oauth2 import service_account
from googleapiclient.discovery import build



# Skapa Flask-applikationen
app = Flask(__name__)
CORS(app)  # Aktivera CORS
db = DatabaseManager('../database/db.sqlite')

# Secret key för JWT
SECRET_KEY = 'din_hemliga_nyckel'

# Funktion för att skydda rutter med JWT-verifiering
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None

        # Kolla om det finns token i Authorization header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Extrahera token
        if not token:
            return jsonify({'message': 'Token saknas!'}), 401

        try:
            # Dekoda token och verifiera den
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user_id = decoded_token['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token har gått ut!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Ogiltig token!'}), 401

        return f(current_user_id, *args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return "Backend för examensarbete är igång!"

@app.route("/api/protected", methods=["GET"])
@token_required
def protected_route(current_user_id):
    # Nu har vi användarens id (current_user_id) som kommer från tokenen
    return jsonify({"message": f"Välkommen användare {current_user_id}!"})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    pin = data.get("pin")

    if not pin:
        return jsonify({"error": "PIN krävs"}), 400

    # Kontrollera användare med den angivna PIN-koden
    user = db.get_user_by_pin(pin)  # Du måste lägga till denna funktion i din DatabaseManager
    if user:
        # Generera ett token och returnera det för frontend
        token = generate_token(user)  # Använd en funktion som genererar en token (JWT eller liknande)
        return jsonify({"status": "success", "token": token, "user": user}), 200
    else:
        return jsonify({"error": "Felaktig PIN"}), 404

def generate_token(user):
    # Generera ett JWT-token med användarens ID och en utgångstid
    expiration = datetime.utcnow() + timedelta(hours=1)  # Token går ut efter 1 timme
    token = jwt.encode(
        {'user_id': user['id'], 'exp': expiration},
        SECRET_KEY,
        algorithm="HS256"
    )
    return token

@app.route("/api/user/<nfc_id>", methods=["GET"])
def get_user_by_nfc(nfc_id):
    print(f"Begäran för användare med NFC-ID: {nfc_id}")  # Logga anropet
    user = db.get_user_by_nfc(nfc_id)
    if user:
        print(f"Hittade användare: {user}")  # Logga användaren som hittades
        return jsonify({"id": user["id"], "name": user["name"]}), 200
    print(f"Användare med NFC-ID {nfc_id} inte hittad.")  # Logga om användaren inte finns
    return jsonify({"error": "User not found"}), 404


@app.route("/api/history", methods=["GET"])
@token_required
def get_history(current_user_id):
    history = db.get_history()
    history_list = [
        {"id": row[0], "user_name": row[1], "action": row[2], "timestamp": row[3]}
        for row in history
    ]
    return jsonify(history_list)

@app.route("/api/history", methods=["POST"])
@token_required
def add_history(current_user_id):
    data = request.json
    action = data.get("action")

    if not action:
        return jsonify({"error": "Action krävs"}), 400

    db.log_history(current_user_id, action)
    return jsonify({"message": "Historik loggad!"}), 201

@app.route("/api/checkin", methods=["POST"])
@token_required
def checkin(current_user_id):
    db.log_history(current_user_id, "check-in")
    return jsonify({'status': 'success', 'message': 'Incheckning registrerad!'})

@app.route("/api/status", methods=["GET"])
@token_required
def get_status(current_user_id):
    history = db.get_user_history(current_user_id)
    if history:
        latest_action = history[0][2]  # Tar den senaste åtgärden
        return jsonify({"status": latest_action}), 200
    return jsonify({"status": "Ingen historik"}), 200

@app.route("/api/change_pin", methods=["POST"])
@token_required
def change_pin(current_user_id):
    data = request.json
    new_pin = data.get("new_pin")

    if not new_pin or len(new_pin) != 4:
        return jsonify({"error": "PIN måste vara exakt 4 siffror"}), 400

    db.update_user_pin(current_user_id, new_pin)
    return jsonify({"message": "PIN-kod uppdaterad!"}), 200



@app.route('/api/calendar', methods=['GET'])
def get_calendar_events():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = 'credentials/examensarbete-458119-1f94e85d5f63.json'
    calendar_id = 'hannes@frikommunikation.se'  # Din kalender-ID eller eventuella group.calendar.google.com ID

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.utcnow().isoformat() + 'Z'
    tomorrow = (datetime.utcnow() + timedelta(days=1)).isoformat() + 'Z'

    print(f"[DEBUG] Hämtar event från {now} till {tomorrow}...")

    events_today = service.events().list(
        calendarId=calendar_id,
        timeMin=now,
        timeMax=tomorrow,
        singleEvents=True,
        orderBy='startTime'
    ).execute().get('items', [])

    print(f"[DEBUG] Events idag: {events_today}")

    if not events_today:
        print("[DEBUG] Inga events idag, testar imorgon...")
        day_after_tomorrow = (datetime.utcnow() + timedelta(days=2)).isoformat() + 'Z'
        events_today = service.events().list(
            calendarId=calendar_id,
            timeMin=tomorrow,
            timeMax=day_after_tomorrow,
            singleEvents=True,
            orderBy='startTime'
        ).execute().get('items', [])
        print(f"[DEBUG] Events imorgon: {events_today}")

    return jsonify(events_today)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)