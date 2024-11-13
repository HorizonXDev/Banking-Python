import json
import os

DATA_FILE = 'bank_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def create_account(username, initial_balance=0):
    data = load_data()
    if username in data:
        return False, "Username already exists"
    data[username] = {'balance': initial_balance}
    save_data(data)
    return True, f"Account created for {username} with balance ${initial_balance}"

def check_balance(username):
    data = load_data()
    if username in data:
        return True, f"Balance for {username}: ${data[username]['balance']}"
    return False, "Account not found"

def deposit(username, amount):
    data = load_data()
    if username in data:
        data[username]['balance'] += amount
        save_data(data)
        return True, f"${amount} deposited into {username}'s account"
    return False, "Account not found"

def withdraw(username, amount):
    data = load_data()
    if username in data:
        if data[username]['balance'] >= amount:
            data[username]['balance'] -= amount
            save_data(data)
            return True, f"${amount} withdrawn from {username}'s account"
        return False, "Insufficient funds"
    return False, "Account not found"
