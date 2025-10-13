import sys
import os
from dotenv import load_dotenv

from scraper import fetch_all_user_data

def main():
    # Load environment variables from .env file
    load_dotenv()

    username = os.getenv("DEV_SODEXO_USER")
    passwd = os.getenv("DEV_SODEXO_PASS")

    # override env if given
    if len(sys.argv) >= 3:
        username, passwd = sys.argv[1:3]
    elif not username or not passwd:
        print("Usage: python scraperTest.py [username] [passwd]")
        sys.exit(1)

    print(f"Fetching data for user: {username}")
    print("=" * 50)

    user_data = fetch_all_user_data(username, passwd)

    if user_data["errors"]:
        print("Errors:")
        for error in user_data["errors"]:
            print(f"  - {error}")

    if user_data["profile"]:
        print(user_data["profile"])
    else:
        print("No user data found")

    if user_data["accounts"]:
        print(f"\nYou have {len(user_data['accounts'])} account(s):")
        print("-" * 50)
        for i, account in enumerate(user_data["accounts"], 1):
            print(f"Account {i}:")
            print(f"  Name: {account.name}")
            print(f"  ID: {account.account_id}")
            print(f"  Balance: ${account.balance:.2f}\n")
    else:
        print("No accounts found.")


if __name__ == "__main__":
    main()
