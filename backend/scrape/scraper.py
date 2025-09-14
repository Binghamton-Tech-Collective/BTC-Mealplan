import requests
from utils import trimToNumbers
from bs4 import BeautifulSoup as Soup
from typing import Optional, List

from endpoints import account_url, sodexo_login_url

class Account:
    #Transactions have not been implemented yet
    def __init__(self, name: str = "", balance: float = 0, accountId: int = 0, transactions: Optional[List] = None):
        self.name = name
        self.balance = balance
        self.accountId = accountId
        self.transactions = transactions

    def __str__(self) -> str:
        return f"{self.name} (id {self.accountId}) | balance: {self.balance}"
    
    #for getters/setters, use account.propertyName

# def generatePayload(username: str, password: str, session: requests.Session) -> str:
#     loginPage = session.get(SODEXO_LOGIN_URL)
# 
#     try:
#         loginPage.raise_for_status()
#     except requests.exceptions.HTTPError as httpErr:
#         print(f"HTTP error occurred\n{httpErr}")
#         kill()        
#     except Exception as err:
#         print(f"An error occurred: {err}")
#         kill()
# 
#     # formInfoValue = Soup(loginPage.text, "html.parser"
#     #     ).find("input", attrs = {"name": "__ncforminfo"} #find form info tag
#     #     ).get("value") #get form info
# 
#     return f""
 
def fetch_login_page(username: str, password: str, session: requests.Session) -> requests.Response:
    response = session.post(sodexo_login_url(username, password))

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as httpErr:
        if response.status_code == 400:
            print(f"Unauthorized\n{httpErr}")
        else:
            print(f"HTTP error occurred\n{httpErr}")
        raise        
    except Exception as err:
        print(f"An error occurred: {err}")
        raise
    if response.text.find("Account Home") == -1:
        print(f"Invalid login details, (response code {response.status_code})")
        raise ValueError("Invalid login details")
        
    return response

def fetch_accounts_data(loginResponse: requests.Response, session: requests.Session) -> List[Account]:
    main_page = Soup(loginResponse.text, "html.parser")
    subTag = main_page.find("strong", string="Account # ")
    tbody = subTag.parent.parent.parent

    accounts = []
    for childTag in tbody.find_all("tr", recursive=False):
        linkTag = childTag.find("a")
        if linkTag != None and linkTag != -1:
            #allTags = list(childTag.children) # possible alternative

            tag1 = childTag.find_next("td").find_next("td") #name
            tag2 = tag1.find_next("td")                     #id
            tag3 = tag2.find_next("td")                     #balance
            
            balanceNumber = float(trimToNumbers(tag3.text))

            account = Account(name=tag1.text, balance=balanceNumber, accountId=int(trimToNumbers(tag2.text)))
            accounts.append(account)
        
    return accounts

def load_account_transaction_history(account: Account, session: requests.Session) -> None:
    response = session.post(account_url(str(account.accountId)))

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as httpErr:
        if response.status_code == 400:
            print(f"Unauthorized\n{httpErr}")
        else:
            print(f"HTTP error occurred\n{httpErr}")
        raise
    except Exception as err:
        print(f"An error occurred: {err}")
        raise

    #todo: load transactions into account class
    
def fetch_account_balance() -> None:
    pass

# test scraper functions
import sys
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: scraper.py [username] [passwd]")
        sys.exit(1)

    (username, passwd) = sys.argv[1:3]
    session = requests.Session()

    accounts = fetch_accounts_data(fetch_login_page(username, passwd, session=session), session)

    print("Found accounts:")
    for acc in accounts:
        print(f"{acc.name} with balance {acc.balance}")
