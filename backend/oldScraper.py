import requests
from bs4 import BeautifulSoup as Soup
import re

SODEXO_LOGIN_URL = "https://bing.campuscardcenter.com/ch/login.html"
ACCOUNT_URL = "https://bing.campuscardcenter.com/ch/accountList.html"
LOGIN_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}

class Account:
    #Transactions have not been implemented yet
    def __init__(self, name: str = "", balance: float = 0, accountId: int = 0, transactions = None):
        self.name = name
        self.balance = balance
        self.accountId = accountId
        self.transactions = transactions

    def getTransactionsLink(self):
        return ACCOUNT_URL + "?id=" + str(self.accountId)

    def __str__(self):
        return f"{self.name} (id {self.accountId}) | balance: {self.balance}"
    
    #for getters/setters, use account.propertyName

def kill():
    print("Program terminated")
    import sys
    sys.exit()

def trimToNumbers(str):
    return re.sub(r"[^\d.]", "", str)

def generatePayload(username, password, session):
    loginPage = session.get(SODEXO_LOGIN_URL)

    try:
        loginPage.raise_for_status()
    except requests.exceptions.HTTPError as httpErr:
        print(f"HTTP error occurred\n{httpErr}")
        kill()        
    except Exception as err:
        print(f"An error occurred: {err}")
        kill()

    formInfoValue = Soup(loginPage.text, "html.parser"
        ).find("input", attrs = {"name": "__ncforminfo"} #find form info tag
        ).get("value") #get form info

    return f"username={username}&password={password}&action=Login&__ncforminfo={formInfoValue}"
 
def new_session():
    return requests.Session()

def fetch_login_page(username: str, password: str, session):
    payload = generatePayload(username, password, session)
    response = session.post(SODEXO_LOGIN_URL, payload, headers=LOGIN_HEADERS)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as httpErr:
        if response.status_code == 400:
            print(f"Unauthorized\n{httpErr}")
        else:
            print(f"HTTP error occurred\n{httpErr}")
        kill()        
    except Exception as err:
        print(f"An error occurred: {err}")
        kill()
    if response.text.find("Account Home") == -1:
        print("Invalid login details")
        kill()
        
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


            account = Account(name=tag1.text, balance=balanceNumber, accountId=int(trimToNumbers(tag2.text)))
            accounts.append(account)
        
    return accounts

def load_account_transaction_history(account: Account, session):
    response = session.post(account.getTransactionsLink())

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as httpErr:
        if response.status_code == 400:
            print(f"Unauthorized\n{httpErr}")
        else:
            print(f"HTTP error occurred\n{httpErr}")
        kill()        
    except Exception as err:
        print(f"An error occurred: {err}")
        kill()

    #todo: load transactions into account class
    
def fetch_account_balance():
    pass