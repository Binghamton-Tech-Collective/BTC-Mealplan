from flask import Flask, jsonify, request
from flask_cors import CORS

import scraper  # You will create this module
import app

# import firebase_admin
# from firebase_admin import credentials, firestore
import scraper  # You will create this module
from dummy_data import *

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Can ignore Firebase for now

# Firebase setup
# cred = credentials.Certificate("firebase-service-account.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

@app.route("/api/get-user-accounts", methods=["POST"])
def get_meal_data():
    # grab user/pass from request body and verify that they are nonempty
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"status": "error", "message": "Username and password required"}), 400


    session = scraper.new_session()
    try:
        loginPage = scraper.fetch_login_page(username, password, session)
        accounts = scraper.fetch_accounts_data(loginPage, session)

        data = list()

        # jsonify can't parse the Account class object, so we manually convert to dictionary instead
        # depending on how future things are implemented, we should factor this function into a utils.py
        for acc in accounts:
            data.append({
                "name" : acc.name,
                "balance" : acc.balance,
                "accountId" : acc.accountId,
                "transactions" : acc.transactions,
            })

        return jsonify({"status": "success", "data": data})
    except Exception as e:
        # TODO: currently this will never trigger b/c scraper.py just kills the program altogether
        # we should raise errors instead so that we can actually send that error message back to the endpoint user
        return jsonify({"status": "error", "message": str(e)}), 500


# endpoints for dummy data
@app.route("/api/dummy/get-transactions", methods=["GET"])
def get_user_transactions():
    return jsonify({"status": "success", "data": dummy_transactions})

@app.route("/api/dummy/get-profile", methods=["GET"])
def get_user_profile():
    return jsonify({"status": "success", "data": dummy_user_data})

@app.route("/api/dummy/get-accounts", methods=["GET"])
def get_user_accounts():
    return jsonify({"status": "success", "data": dummy_accounts_data})


if __name__ == "__main__":
    app.run(debug=True)