import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from ../.env
load_dotenv()

# Grab Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

# Create the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

res = supabase.table("users").select("*").execute()
print(res)