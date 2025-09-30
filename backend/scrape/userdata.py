from typing import Optional, List
from backend.scrape.account import Account
from backend.scrape.card import Card
class UserData:
    def __init__(self,
        name: str = "", phone_number: int = -1, email: str = None, 
        accounts: Optional[List[Account]] = None,
        cards: Optional[List[Card]] = None
    ):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.accounts = accounts
        self.cards = cards

