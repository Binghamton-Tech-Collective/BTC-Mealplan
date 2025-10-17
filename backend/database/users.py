from client import supabase
from utils import remove_none_values

# https://supabase.com/docs/reference/python/introduction
# ^ this link is a great place to start to understand how to interact with Supabase in Python
# ^ note that the client is already set up in client.py and imported as 'supabase'

# EXAMPLE FUNCTION
def get_all_users():
    res = supabase.table("users").select("*").execute()
    if res.error:
        raise Exception(res.error.message)
    return res.data


# Task 2: implement basic CRUD: Create, Read, Update, Delete
def create_user(id=None, first_name=None, last_name=None, email=None, phone_number=None):
    # parameters should be id, first_name, last_name, email, and phone
    # note that some of these values can be null and can be undefined
    
    userData = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number
    }

    # remove none values to allow supabase defaults
    userData = remove_none_values(userData)

    try:
        res = supabase.table("users").insert(userData).execute()

        # output should create a row in the users table and return that user object
        return res.data[0] if res.data else None
    except Exception as e:
        raise Exception(f"Error creating user: {str(e)}")


def get_user_by_id(user_id=None):
    # parameter should be user_id
    if user_id is None:
        return None # No ID provided
    
    try:
        res = supabase.table("users").select("*").eq("id", user_id).single().execute()

        # return the user object with the corresponding id
        # if no valid user, you should return null/none
        return res.data if res.data else None
    except Exception as e:
        raise Exception(f"Error fetching user from user_id ({user_id}): {str(e)}")


def update_user(user_id=None, **kwargs):
    # parameters should be user_id [this is the user row that we want to modify]
    # followed by the various columns we may want to update (name, email, phone, etc.)
    if user_id is None:
        return None # No ID provided
    
    # filter out None values - only update fields that are explicitly provided
    updateData = remove_none_values(kwargs)

    if not updateData:
        return None # nothing to update

    try:
        res = supabase.table("users").update(updateData).eq("id", user_id).execute()

        # return the updated user
        return res.data[0] if res.data else None
    except Exception as e:
        raise Exception(f"Error updating user {user_id}: {str(e)}")


def delete_user():
    # more complex, hold off for now
    pass
