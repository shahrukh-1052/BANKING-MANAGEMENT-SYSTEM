# register.py
from customer import *
from bank import Bank
import random

def SignUp():
    username = input("Create Username: ").strip()
    existing = db_query(f"SELECT username FROM customers WHERE username = '{username}';")

    if existing:
        print(" Username already exists! Try another.\n")
        return

    print(" Username available. Please proceed.")
    password = input("Enter Your Password: ").strip()
    name = input("Enter Your Name: ").strip()
    age = input("Enter Your Age: ").strip()
    city = input("Enter Your City: ").strip()

    # Generate unique account number
    while True:
        account_number = random.randint(10000000, 99999999)
        check = db_query(f"SELECT account_number FROM customers WHERE account_number = {account_number};")
        if not check:
            print(f"Your new Account Number: {account_number}")
            break

    # Create customer record and transaction table
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    print(" Account successfully created!\n")

def SignIn():
    username = input("Enter Username: ").strip()
    temp = db_query(f"SELECT password, name FROM customers WHERE username = '{username}';")

    if not temp:
        print(" Username not found. Please sign up first.\n")
        return None

    while True:
        password = input("Enter Password: ").strip()
        if password == temp[0][0]:
            print(f" Sign In Successful! Welcome, {temp[0][1].capitalize()}.\n")
            return username
        else:
            print(" Incorrect password. Try again.")
