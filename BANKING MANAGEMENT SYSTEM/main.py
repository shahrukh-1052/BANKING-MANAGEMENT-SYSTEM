# main.py
from register import *
from bank import *

print(" Welcome to SHAHRUKH Banking System!\n")

status = False
user = None

while True:
    try:
        print("1. Sign Up")
        print("2. Sign In")
        choice = int(input("Enter your choice (1 or 2): "))
        if choice == 1:
            SignUp()
        elif choice == 2:
            user = SignIn()
            if user:
                status = True
                break
        else:
            print("Please enter 1 or 2 only.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

if status:
    account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")[0][0]

    while True:
        try:
            option = int(input(
                "\nChoose Service:\n"
                "1. Balance Enquiry\n"
                "2. Cash Deposit\n"
                "3. Cash Withdraw\n"
                "4. Fund Transfer\n"
                "5. View Transaction History\n"
                "6. Exit\n"
                "Enter your choice: "
            ))

            bobj = Bank(user, account_number)

            if option == 1:
                bobj.balanceenquiry()
            elif option == 2:
                amt = int(input("Enter amount to deposit: "))
                bobj.deposit(amt)
            elif option == 3:
                amt = int(input("Enter amount to withdraw: "))
                bobj.withdraw(amt)
            elif option == 4:
                recv = int(input("Enter receiver account number: "))
                amt = int(input("Enter amount to transfer: "))
                bobj.fundtransfer(recv, amt)
            elif option == 5:
                bobj = Bank(user, account_number)
                bobj.view_transaction_history()
            elif option == 6:
                print(" Thank you for using SHAHRUKH Banking Services!")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.\n")
