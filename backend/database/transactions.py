# See users.py for more info
from client import supabase
from accounts import get_dummy_accounts_data
from collections import defaultdict

def get_dummy_transactions_data(user_id=None):
    # no parameters, should just return all the transactions that belong to a user

    if user_id is None:
        return None
    
    try:
        accounts = get_dummy_accounts_data(user_id) # get all accounts belonging to this user

        if not accounts:
            return {} # no accounts found
        
        account_ids = [account["id"] for account in accounts] # extract account ids

        # get only transactions that belong to these accounts
        res = supabase.table("transactions").select("*").in_("account_id", account_ids).execute()

        transactions = res.data or []

        # group transactions by account_id
        grouped = defaultdict(list)
        for txn in transactions:
            grouped[txn["account_id"]].append(txn)
        
        # you probably want to return a dictionary with key-val pairs of (account_id: list[transactions])
        return dict(grouped)

    except Exception as e:
        raise Exception(f"Error fetching transactions for user {user_id}: {str(e)}")