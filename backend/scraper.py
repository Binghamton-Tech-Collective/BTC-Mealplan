# scraper_boilerplate.py

import requests

# ----------------------------
# Constants / Config
# ----------------------------
SODEXO_LOGIN_URL = "https://bing.campuscardcenter.com/ch/login.html"
ACCOUNT_URL = "https://bing.campuscardcenter.com/ch/accountList.html"
LOGIN_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}

# ----------------------------
# Helper functions
# ----------------------------
def new_session():
    """Return a new requests session"""
    return requests.Session()

def login(username, password, session):
    """Perform login and return login page response"""
    # TODO: implement login
    pass

def fetch_accounts(login_response, session):
    """Fetch list of accounts"""
    # TODO: implement account scraping
    pass

def fetch_transactions(account, session):
    """Fetch transaction history for one account"""
    # TODO: implement transaction scraping
    pass

# ----------------------------
# Coordinator / Flow
# ----------------------------
def fetch_all_user_data(username, password, fetch_transactions=True):
    """
    Placeholder coordinator function:
    - Login once
    - Fetch accounts
    - Optionally fetch transactions per account
    - Return structured data
    """
    session = new_session()
    result = {"accounts": [], "errors": []}

    # 1. Login
    try:
        login_response = login(username, password, session)
    except Exception as e:
        result["errors"].append(f"Login failed: {e}")
        return result

    # 2. Fetch accounts
    try:
        accounts = fetch_accounts(login_response, session)
        result["accounts"] = accounts
    except Exception as e:
        result["errors"].append(f"Failed to fetch accounts: {e}")
        accounts = []

    # Add other helper functions later

    return result
