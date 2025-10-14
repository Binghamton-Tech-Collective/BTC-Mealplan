from typing import Optional, List
from transaction import Transaction

class Account:
    #Transactions have not been implemented yet
    def __init__(self, name: str = "", balance: float = 0, account_id: int = 0, transactions: Optional[List[Transaction]] = None):
        self.name = name
        self.balance = balance
        self.account_id = account_id
        self.transactions = transactions

    def __str__(self) -> str:
        return f"{self.name} (id {self.account_id}) | balance: {self.balance}"
    
    #for getters/setters, use account.propertyName