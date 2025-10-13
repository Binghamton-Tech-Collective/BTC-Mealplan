from client import supabase


# https://supabase.com/docs/reference/python/introduction
# ^ this link is a great place to start to understand how to interact with Supabase in Python
# ^ note that the client is already set up in client.py and imported as 'supabase'

# EXAMPLE FUNCTION
def get_all_users():
    res = supabase.table("users").select("*").execute()
    if res.error:
        raise Exception(res.error.message)
    return res.data

# Task 1: write dummy data reads for Supabase
def get_dummy_user_data():
    # no parameters, should just return the row in our table that refers to the admin
    pass

# Task 2: implement basic CRUD: Create, Read, Update, Delete
def create_user():
    # parameters should be id, first_name, last_name, email, and phone
    # note that some of these values can be null and can be undefined

    # output should create a row in the users table and return that user object
    pass

def get_user_by_id():
    # parameter should be user_id

    # return the user object with the corresponding id
    # if no valid user, you should return null/none
    pass

def update_user():
    # parameters should be user_id [this is the user row that we want to modify]
    # followed by the various columns we may want to update (name, email, phone, etc.)

    # return the updated user
    pass


def delete_user():
    # more complex, hold off for now
    pass
