import re

def trimToNumbers(string: str) -> str:
    return re.sub(r"[^\d.]", "", string)

