from typing import Optional, List
from account import Account
from card import Card
class Profile:
    def __init__(self,
        name: str = "", phone_number: int = -1, email: str = ""
    ):
        self.name = name
        self.phone_number = phone_number
        self.email = email

