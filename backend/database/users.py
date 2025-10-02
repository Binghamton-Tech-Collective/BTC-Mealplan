from client import supabase

def get_all_users():
    res = supabase.table("users").select("*").execute()
    if res.error:
        raise Exception(res.error.message)
    return res.data


def get_user_by_id():
    pass


def create_user():
    pass


def update_user():
    pass


def delete_user():
    pass
