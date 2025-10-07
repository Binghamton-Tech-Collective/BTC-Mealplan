def login():
    # parameters should be user, pass, access_token, refresh_token

    # 1. check if access_token is valid, if so, this will return a auth.user and we should return this auth.user (this should contain session data about token info)

    # 2. if access_token fails, try refreshing the session using refresh_token
    # if this works, it will return a valid auth.user, follow same flow as #1

    # 3. if neither tokens are good, we want to use the user/pass and call the update function
    # the update function will give us back a public.user object, we can use this to retrieve the auth.user
    # NOTE: not sure if you can directly retrieve a auth.user with an id, if you can that's probably the simplest
    # if not, worst case you would just login manually with supabase.auth.sign_in_with_password()
    pass

def update():
    # parameter should be user/pass

    # 1. call the fetch_all_data function from /scrape

    # 2. use this data to get the user email
    # 3. the user email should be a unique identifier. use this to check if we have a row in our users.table with this email
    
    # 3b. if the row exists, skip 3a.

    # 3a. if that row doesn't exist, we have to create the a user in our database. This involves a few steps:
    # - first, you have to make a auth.user, do this with supabase.auth.sign_in_with_password(). 
    # - NOTE: we need to discuss this section, i think barebones, we can just include a password in our .env and use that for every user
    # - however, this isn't great security, kinda asking you to figure this part out lol. wouldn't be unreasonable to create a random passwd str for each user as a new column, hash it and use that as the passwd
    # - once you make the auth.user, you have to make a row in our public.users table that references the auth.user.id as a foreign key

    # 4. upsert the data (upsert means to create if it doesn't exist, otherwise simply update)

    # 5. return the public.user object
    pass


# write a script to test it, feel free to place it in a different file, call it pipelineTest.py or something like that

# update() should be easy to test, just call it user/pass from .env and then check the database to see if the data was updated
# if you want to go above and beyond, you can do that here in code instead of manually check the database

# to test login, you need to try a few different approaches
# 1. fresh user, no tokens. basically just enter in a user/pass see if it returns a valid auth.user and if it writes to our database
# 2. valid access_token. expected behavior should just be getting a auth.user (should be no updates in the database)
# 3. invalid access_token, valid refresh_token. expected behavior should be the same as option 2
