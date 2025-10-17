# See users.py for more info
from client import supabase
from typing import List
from accounts import get_accounts_by_user_id

def get_transactions_by_user_id(user_id: str) -> List[dict]:
    # no parameters, should just return all the transactions that belong to a user

    if user_id is None:
        return []
    
    try:
        accounts = get_accounts_by_user_id(user_id) # get all accounts belonging to this user

        if not accounts:
            return [] # no accounts found
        
        account_ids = [account["id"] for account in accounts] # extract account ids

        # get only transactions that belong to these accounts
        res = supabase.table("transactions").select("*").in_("account_id", account_ids).execute()

        return res.data or []

    except Exception as e:
        raise Exception(f"Error fetching transactions for user {user_id}: {str(e)}")