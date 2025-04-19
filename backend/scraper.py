import requests
from bs4 import BeautifulSoup as Soup
import re

import utils

SODEXO_LOGIN_URL = "https://bing.campuscardcenter.com/ch/login.html"
LOGIN_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}

def trimToNumbers(str):
    return re.sub(r"[^\d.]", "", str)

def generatePayload(username, password, session):
    loginPage = session.get(SODEXO_LOGIN_URL)

    try:
        loginPage.raise_for_status()
    except requests.exceptions.HTTPError as httpErr:
        raise httpErr     
    except Exception as err:
        raise err
    formInfoValue = Soup(loginPage.text, "html.parser"
        ).find("input", attrs = {"name": "__ncforminfo"} #find form info tag
        ).get("value") #get form info

    return f"username={username}&password={password}&action=Login&__ncforminfo={formInfoValue}"
 
def new_session():
    return requests.Session()

def fetch_login_page(username: str, password: str, session):
    payload = generatePayload(username, password, session)
    response = session.post(SODEXO_LOGIN_URL, payload, headers=LOGIN_HEADERS)
    response.raise_for_status()
    if response.text.find("Account Home") == -1:
        raise Exception("Invalid login details")
        
    return response

def fetch_accounts_data(loginResponse, session):
    mainPage_soup = Soup(loginResponse.text, "html.parser")
    subTag = mainPage_soup.find("strong", string = "Account # ")
    tbody = subTag.parent.parent.parent

    accounts = []
    for childTag in tbody.find_all("tr", recursive=False):
        linkTag = childTag.find("a")
        if linkTag != None and linkTag != -1:
            #allTags = list(childTag.children) # possible alternative

            tag1 = childTag.find_next("td").find_next("td") #name
            tag2 = tag1.find_next("td") #id
            tag3 = tag2.find_next("td") #balance
            
            balanceNumber = float(trimToNumbers(tag3.text))


            account = utils.Account(name=tag1.text, balance=balanceNumber, accountId=int(trimToNumbers(tag2.text)))
            accounts.append(account)
        
    return accounts

def load_account_transactions(account: utils.Account, session):
    response = session.post(account.getTransactionsLink())
    response.raise_for_status()

    # todo: load transactions into account class, now that the webpage for transactions have loaded
    # use utils.Transaction to save one transaction data, 
    soup = Soup(response, "html.parser")
    transactionsTable = soup.find("tbody")

    for tag in transactionsTable.find_next_siblings("tr", attrs = {"id": "EntryRow"}):
        pass
