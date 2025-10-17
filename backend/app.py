from flask import Flask, jsonify, request
from flask_cors import CORS
import scraper  # You will create this module
from dummy_data import *
from database.users import get_user_by_id
from database.transactions import get_transactions_by_user_id
from database.accounts import get_accounts_by_user_id
import os

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Can ignore Firebase for now

# Firebase setup
# cred = credentials.Certificate("firebase-service-account.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

@app.route("/api/accounts", methods=["POST"])
def get_meal_data():
    # TODO: This endpoint is currently deprecated
    # # grab user/pass from request body and verify that they are nonempty
    # data = request.json
    # username = data.get("username")
    # password = data.get("password")

    # if not username or not password:
    #     return jsonify({"status": "error", "message": "Username and password required"}), 400


    # session = scraper.new_session()
    # try:
    #     loginPage = scraper.fetch_login_page(username, password, session)
    #     accounts = scraper.fetch_accounts_data(loginPage, session)

    #     data = list()

    #     # jsonify can't parse the Account class object, so we manually convert to dictionary instead
    #     # depending on how future things are implemented, we should factor this function into a utils.py
    #     for acc in accounts:
    #         data.append({
    #             "name" : acc.name,
    #             "balance" : acc.balance,
    #             "accountId" : acc.accountId,
    #             "transactions" : acc.transactions,
    #         })

    #     return jsonify({"status": "success", "data": data})
    # except Exception as e:
    #     # TODO: currently this will never trigger b/c scraper.py just kills the program altogether
    #     # we should raise errors instead so that we can actually send that error message back to the endpoint user
    #     return jsonify({"status": "error", "message": str(e)}), 500
    pass


# Task 1: reroute these endpoints to call the supabase dummy functions you implement
# after you do that, you can delete dummy_data.py
@app.route("/api/dummy/transactions", methods=["GET"])
def get_user_transactions():
    try:
        admin_id = os.getenv("ADMIN_ID")
        if not admin_id:
            return jsonify({"status": "error", "message": "ADMIN_ID not configured"})
        
        transactions = get_transactions_by_user_id(admin_id)
        return jsonify({"status": "success", "data": transactions})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/api/dummy/profile", methods=["GET"])
def get_user_profile():
    try:
        admin_id = os.getenv("ADMIN_ID")
        if not admin_id:
            return jsonify({"status": "error", "message": "ADMIN_ID not configured"})
        
        user = get_user_by_id(admin_id)
        if not user:
            return jsonify({"status": "error", "message": "User not found"})
        
        return jsonify({"status": "success", "data": user})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/api/dummy/accounts", methods=["GET"])
def get_user_accounts():
    try:
        admin_id = os.getenv("ADMIN_ID")
        if not admin_id:
            return jsonify({"status": "error", "message": "ADMIN_ID not configured"})
        
        accounts = get_accounts_by_user_id(admin_id)
        return jsonify({"status": "success", "data": accounts})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
