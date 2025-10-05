import re
import requests
from utils import trimToNumbers
from bs4 import BeautifulSoup as Soup
from typing import List

from endpoints import account_url, sodexo_login_url, profile_url
from account import Account
from card import Card
from profile import Profile

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

#idea is for fetch_profile to populate a given Profile, and maybe the rest of the functions could follow this style. unsure whether to pass in an empty Profile to then put into a main Profile or just pass in a main Profile, but both seem viable.
def fetch_profile(session: requests.Session) -> Profile:
    response = session.get(profile_url())
    
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

    if response.text.find("Personal Information") == -1:
        print(f"Failed to reach site, bad cookies? (response code {response.status_code})")
        raise
    page = Soup(response.text, "html.parser")
    main_tag = page.find("div", class_="feature")
    tbody_tag = main_tag.find("table")

    profile = Profile()
    
    for tr_tag in tbody_tag.find_all("tr", string="", recursive=False):
        st = tr_tag.find("strong")
        if st == None:
            continue
        
        infoType = st.text
        if infoType.find(":") == -1:
            continue

        print("new tr of infotype", infoType)
        if (infoType.find("Name") != -1):
            for td_tag in tr_tag.find_all("td", string=True, resursive=False):
                infoText = td_tag.get_text(strip=True)
                
                if (infoText != "> Edit" and infoText != "Name :"):
                    profile.name=infoText

        elif (infoType.find("Phone") != -1):
            td_tag = tr_tag.find("td")
            infoText = td_tag.get_text(strip=True)
            
            if (infoText != ""):
                profile.phone_number = int(infoText)

        elif (infoType.find("Email") != -1):
            for td_tag in tr_tag.find_all("td", string=True, resursive=False):
                infoText = td_tag.get_text(strip=True)
            
                if (infoText.find("@") != -1):
                    profile.email = infoText

    print(profile.__dict__)          
    return profile

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

def fetch_transactions(account, session:requests.Session):
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
    - Fetch profile
    - Fetch accounts
    - Optionally fetch transactions per account
    - Return structured data
    """
    session = requests.Session()
    result = {"accounts": [], "profile": [], "errors": []}

    # 1. Login
    try:
        login_response = login(username, password, session)
    except Exception as e:
        result["errors"].append(f"Login failed: {e}")
        return result

    # 2. Fetch profile
    try:
        profile = fetch_profile(session)
        result["profile"] = profile
    except Exception as e:
        result["errors"].append(f"Failed to fetch profile: {e}")
        profile = []

    # 3. Fetch accounts
    try:
        accounts = fetch_accounts(login_response, session)
        result["accounts"] = accounts
    except Exception as e:
        result["errors"].append(f"Failed to fetch accounts: {e}")
        accounts = []

    # Add other functions later

    return result

# test scraper functions
import sys
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: scraper.py [username] [passwd]")
        sys.exit(1)

    (username, passwd) = sys.argv[1:3]
    session = requests.Session()

    user_data = fetch_all_user_data(username, passwd)

    print(f"recv data {user_data}")


