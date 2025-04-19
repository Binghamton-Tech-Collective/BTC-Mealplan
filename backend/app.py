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

def loadCredentials():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    return (username, password)


@app.route("/api/get-user-accounts", methods=["POST"])
def get_account_data():
    # grab user/pass from request body and verify that they are nonempty
    (username, password) = loadCredentials()

    if not username or not password:
        return jsonify({"status": "error", "message": "Username and password required"}), 400


    session = scraper.new_session()
    # im considering getting succcessful login sessions with get_auth() or something
    # and saving it to a variable outside of this function's scope for use in other functions
    # to prevent needing to create + delete many sessions

    try:
        loginPage = scraper.fetch_login_page(username, password, session)
        accounts = scraper.fetch_accounts_data(loginPage, session)

        session.close()

        data = {} 
        # maybe easier (?) for front end using this format where the keys are accountid strings:
        # { accountId : {"balance": 500, "name" : "Example", "accountId" : accountId} }

        for acc in accounts:
            id = str( getattr(acc, "accountId", -1) )
            data[id] = acc.getAccountOverviewDict()

        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
def get_account_transactions(accounts): #expects a list of Account objects
    (username, password) = loadCredentials()
    
    session = scraper.new_session()

    try:
        scraper.fetch_login_page(username, password, session) # authorize session
        data = {}

        for account in accounts:
            accountTransactions = scraper.load_account_transactions(account, session)
            data[str(getattr(account, "accountId"))] = { accountTransactions }

        session.close()

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