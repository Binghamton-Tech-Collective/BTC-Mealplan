import re
import requests
from utils import trimToNumbers
from bs4 import BeautifulSoup as Soup
from typing import List

from endpoints import account_url, sodexo_login_url
from account import Account

def login(username, password, session: requests.Session):
    """Performs login and returns login page response"""
    response = session.post(sodexo_login_url(username, password))

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 400:
            print(f"Unauthorized\n{http_err}")
        else:
            print(f"HTTP error occurred\n{http_err}")
        raise        
    except Exception as err:
        print(f"An error occurred: {err}")
        raise
    if response.text.find("Account Home") == -1:
        print(f"Invalid login details, (response code {response.status_code})")
        raise ValueError("Invalid login details")
        
    return response

def fetch_accounts(login_response, session: requests.Session) -> List[Account]:
    """Fetches a list of accounts"""
    main_page = Soup(login_response.text, "html.parser")
    sub_tag = main_page.find("strong", string="Account # ")
    tbody = sub_tag.parent.parent.parent

    accounts = []
    for child_tag in tbody.find_all("tr", recursive=False):
        link_tag = child_tag.find("a")
        if link_tag != None and link_tag != -1:
            #all_tags = list(child_tag.children) # possible alternative

            tag1 = child_tag.find_next("td").find_next("td") #name
            tag2 = tag1.find_next("td")                      #id
            tag3 = tag2.find_next("td")                      #balance
            
            balance_number = float(trimToNumbers(tag3.text))

            account = Account(name=tag1.text, balance=balance_number, account_id=int(trimToNumbers(tag2.text)))
            accounts.append(account)
        
    return accounts

def fetch_transactions(account, session):
    """Fetch transaction history for one account"""
    # TODO: finish transaction scraping
    response = session.post(account_url(str(account.account_id)))

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 400:
            print(f"Unauthorized\n{http_err}")
        else:
            print(f"HTTP error occurred\n{http_err}")
        raise
    except Exception as err:
        print(f"An error occurred: {err}")
        raise

    #todo: load transactions into account class
    pass

def fetch_all_user_data(username, password, fetch_transactions=True):
    """
    Placeholder coordinator function:
    - Login once
    - Fetch accounts
    - Optionally fetch transactions per account
    - Return structured data
    """
    session = requests.Session()
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

    # Add other functions later

    return result

# test scraper functions
if __name__ == "__main__":
    import sys
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()
    
    username = os.getenv("DEV_SODEXO_USER")
    passwd = os.getenv("DEV_SODEXO_PASS")

    # override env if given
    if len(sys.argv) >= 3:
        username, passwd = sys.argv[1:3]
    elif not username or not passwd:
        print("Usage: scraper.py [username] [passwd]")
        sys.exit(1)

    session = requests.Session()

    user_data = fetch_all_user_data(username, passwd)

    print(f"recv data {user_data}")
    for account in user_data["accounts"]:
        print(account)


