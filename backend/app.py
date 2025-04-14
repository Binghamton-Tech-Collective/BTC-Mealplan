from InquirerPy import inquirer

from flask import Flask, jsonify, request
# from flask_cors import CORS

import scraper  # You will create this module
import app

# import firebase_admin
# from firebase_admin import credentials, firestore

# app = Flask(__name__)
# CORS(app)  # Enable cross-origin requests

# Can ignore Firebase for now

# Firebase setup
# cred = credentials.Certificate("firebase-service-account.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# @app.route("/api/meal-data", methods=["POST"])
def get_meal_data():
    username = inquirer.text(
        message="Enter your username:"
    ).execute()

    password = inquirer.secret(
        message="Enter your password:"
    ).execute()
    
    session = scraper.new_session()
    loginPage = scraper.fetch_login_page(username, password, session)
    accounts = scraper.fetch_accounts_data(loginPage, session)

    #See scraper.py's Account class for info on retrieving data through python, otherwise jsonify should do it for you

    # print("\Your current accounts:")
    # for acc in accounts:
    #     print("\t"+str(acc))

    #scraper.load_account_transaction_history(accounts[0], session)
    
    return jsonify({"status": "success", "data": accounts}) #working on error handling later
    # try:
    #     meal_data = scraper.fetch_meal_data(username, password)
    #     return jsonify({"status": "success", "data": meal_data})
    # except Exception as e:
    #     return jsonify({"status": "error", "message": str(e)}), 500

def run(debug):
    get_meal_data()
if __name__ == "__main__":
    app.run(debug=True)