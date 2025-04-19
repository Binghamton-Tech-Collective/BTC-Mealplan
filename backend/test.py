from InquirerPy import inquirer #for future testing, waiting on next meeting to discuss .env.
import app

def test_login():
    
    returnData = app.get_account_data()
    print(returnData) 

def run_test():
    test_login()

run_test()