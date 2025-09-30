from typing import TypedDict


class Card(TypedDict):
    card_number: int
    active: bool = False