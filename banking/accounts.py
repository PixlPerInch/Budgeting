account = {"holder": "","number": "1234","balance": 0}

def setup_account(name, initial_balance):
    account["holder"] = name
    account["balance"] = initial_balance

def get_account_details():
    return "Holder: " + account["holder"] + " | Account No: " + account["number"]

def check_balance():
    return "Current Balance:  " + str(round(account["balance"], 2))

def deposit(amount):
    if amount <= 0:
        return "Invalid deposit amount."
    
    account["balance"] = account["balance"] + amount
    return "Successfully deposited:  " + str(round(amount, 2))

def withdraw(amount):
    if amount <= 0:
        return "Invalid withdrawal amount."
    if amount > account["balance"]:
        return "Insufficient funds."
        
    account["balance"] = account["balance"] - amount
    return "Successfully withdrew:  " + str(round(amount, 2))