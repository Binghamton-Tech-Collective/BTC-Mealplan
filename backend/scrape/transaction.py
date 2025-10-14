
class Transaction():
    def __init__(self,
        id: int,
        date: str,
        method: str, #labeled "type" column on the site
        description: str,
        amount: int,
        approval_id: int,
        settled_date: str,
    ):
        
        self.id = id
        self.date = date
        self.method = method
        self.description = description
        self.amount = amount
        self.approval_id = approval_id
        self.settled_date = settled_date