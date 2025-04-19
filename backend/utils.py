
class Transaction:
    def __init__(self, id: int, date: str, time_of_day: str, description: str, amount: float, settled_date: str):
        self.id = id                        # transaction-specific ID
        self.date = date                    # day of transaction, ex: "Apr 3, 2025"
        self.time_of_day = time_of_day      # in format of something, ex: "12:25 PM"
        self.description = description
        self.amount = amount                # money gained (negative if spent)
        self.settled_date = settled_date    # day transaction settled
    
    def getDict(self):
        return {
            "id": self.id,
            "date": self.date,
            "time": self.time_of_day,
            "description": self.description,
            "amount": self.amount,
            "settledDate": self. settled_date,
            "type": "PTS",      # unsure what this is
        }
    
class Account:
    _ACCOUNT_URL = "https://bing.campuscardcenter.com/ch/accountList.html"
    _accounts = []

    @staticmethod
    def getAccounts(): #gives all account objects
        return Account._accounts
    
    def __init__(self, name: str = "", balance: float = 0, accountId: int = 0, transactions = []):
        self.name = name
        self.balance = balance
        self.accountId = accountId
        self.transactions = transactions

        Account._accounts.append(self)

    def getTransactionsLink(self):
        return Account._ACCOUNT_URL + "?id=" + str(self.accountId)
    
    def addTransaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def sortTransactions():
        pass

    def getTransactionsList(self):
        list = []
        for t in self.transactions:
            list.append(t.getDict())
            
        return list

    def getAccountOverviewDict(self):
        return {
            "name" : self.name,
            "balance" : self.balance,
            "accountId" : self.accountId
        }
    
    def __str__(self):
        return f"{self.name} (id {self.accountId}) | balance: {self.balance}"

