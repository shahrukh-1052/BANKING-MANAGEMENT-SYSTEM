# Bank Services (Revised for Central Transaction History Table)
from database import *
import datetime

class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    # Show Balance
    def balanceenquiry(self):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        print(f"{self.__username} Balance is {temp[0][0]}")

    # Deposit Money
    def deposit(self, amount):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        new_balance = temp[0][0] + amount
        db_query(
            f"UPDATE customers SET balance = {new_balance} WHERE username = '{self.__username}';")
        mydb.commit()

        # Record transaction
        db_query(
            f"INSERT INTO transaction_history (username, transaction_type, amount) "
            f"VALUES ('{self.__username}', 'DEPOSIT', {amount});")
        mydb.commit()

        print(f"Amount ₹{amount} Deposited Successfully!")
        self.balanceenquiry()

    # Withdraw Money
    def withdraw(self, amount):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print(" Insufficient Balance!")
        else:
            new_balance = temp[0][0] - amount
            db_query(
                f"UPDATE customers SET balance = {new_balance} WHERE username = '{self.__username}';")
            mydb.commit()

            db_query(
                f"INSERT INTO transaction_history (username, transaction_type, amount) "
                f"VALUES ('{self.__username}', 'WITHDRAW', {amount});")
            mydb.commit()

            print(f"Amount ₹{amount} Withdrawn Successfully!")
            self.balanceenquiry()

    # Fund Transfer
    def fundtransfer(self, receiver_acc, amount):
        sender_balance = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount > sender_balance[0][0]:
            print(" Insufficient Balance!")
            return

        receiver = db_query(
            f"SELECT username, balance FROM customers WHERE account_number = {receiver_acc};")
        if not receiver:
            print(" Receiver account not found.")
            return

        receiver_username, receiver_balance = receiver[0]
        new_sender_balance = sender_balance[0][0] - amount
        new_receiver_balance = receiver_balance + amount

        db_query(
            f"UPDATE customers SET balance = {new_sender_balance} WHERE username = '{self.__username}';")
        db_query(
            f"UPDATE customers SET balance = {new_receiver_balance} WHERE account_number = {receiver_acc};")
        mydb.commit()

        # Record transactions
        db_query(
            f"INSERT INTO transaction_history (username, transaction_type, amount) "
            f"VALUES ('{self.__username}', 'TRANSFER_OUT', {amount});")
        db_query(
            f"INSERT INTO transaction_history (username, transaction_type, amount) "
            f"VALUES ('{receiver_username}', 'TRANSFER_IN', {amount});")
        mydb.commit()

        print(f" ₹{amount} transferred successfully to account {receiver_acc}!")

    # View Transaction History
    def view_transaction_history(self):
        history = db_query(
            f"SELECT transaction_type, amount, transaction_date FROM transaction_history "
            f"WHERE username = '{self.__username}' ORDER BY transaction_date DESC;")
        if not history:
            print("No transactions found.")
            return
        print(f"\nTransaction History for {self.__username}:")
        for t in history:
            print(f"{t[2]} | {t[0]} | ₹{t[1]}")
