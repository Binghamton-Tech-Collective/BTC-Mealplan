# See users.py for more info
from client import supabase
from typing import List

def get_accounts_by_user_id(user_id: str) -> List[dict]:
    # no parameters, should just return all the accounts that belong to admin

    # no user_id is given
    if user_id is None:
        return None
    
    # output should probably just be a list of Accounts
    try:
        # returns a list of every Account object that belongs to the user_id
        res = supabase.table("accounts").select("*").eq("user_id", user_id).execute()
        return res.data or []
    except Exception as e:
        raise Exception(f"Error fetching accounts for {user_id}: {str(e)}")