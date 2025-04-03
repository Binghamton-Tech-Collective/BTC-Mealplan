from flask import Flask, jsonify, request
from flask_cors import CORS
# import firebase_admin
# from firebase_admin import credentials, firestore
import scraper  # You will create this module

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests


# Can ignore Firebase for now

# Firebase setup
# cred = credentials.Certificate("firebase-service-account.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

@app.route("/api/meal-data", methods=["POST"])
def get_meal_data():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    try:
        meal_data = scraper.fetch_meal_data(username, password)
        return jsonify({"status": "success", "data": meal_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)