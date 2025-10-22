
# 🏦 Banking Management System

Welcome to the **Banking Management System**, a Python-based command-line application that provides complete digital banking functionality — including account creation, balance management, deposits, withdrawals, fund transfers, and transaction tracking.  
This project demonstrates secure database handling, modular design, and the use of Object-Oriented Programming (OOP) principles.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Database Setup](#database-setup)
   - [Installation](#installation)
   - [Usage](#usage)
5. [Code Overview](#code-overview)
6. [Future Enhancements](#future-enhancements)
7. [Contributing](#contributing)
8. [Contact](#contact)

---

## 🧾 Overview

The **Banking Management System** simulates a real-world banking environment through a terminal-based interface.  
Each user can create an account, perform transactions, and view a detailed transaction history.  
All data is securely stored in a MySQL database with automatic timestamp tracking for each transaction.

---

## ⚙️ Features

### 🔐 User Authentication
- Sign Up: Register a new customer account.
- Sign In: Log in securely with username and password validation.

### 💼 Account Management
- Create and manage bank accounts.
- Each account has a **unique account number**.
- Accounts include balance and customer details (name, age, city, etc.).

### 💰 Transactions
- Deposit and withdraw money.
- Transfer funds to another user’s account.
- View full transaction history with timestamp and transaction type.

### 🧾 Transaction History
- All activities (Deposit, Withdraw, Transfer) are logged in the **transaction_history** table.
- Automatically records:
  - Username
  - Transaction type (DEPOSIT, WITHDRAW, TRANSFER_IN, TRANSFER_OUT)
  - Amount
  - Date and time (auto-generated)

### 🧩 Database Features
- **customers** table for storing user info and account details.
- **transaction_history** table for storing detailed transaction logs.
- Automatic timestamp and foreign key constraints for data consistency.

---

## 🧱 Project Structure

```

BANKING MANAGEMENT SYSTEM/
│
├── bank.py                  # Core banking operations (deposit, withdraw, transfer, etc.)
├── customer.py              # Customer-related class definitions
├── register.py              # Handles Sign Up and user registration
├── main.py                  # Entry point of the application (menu-based interface)
├── database.py              # Handles MySQL database connectivity and queries
├── bnksysmgmt.sql           # SQL script for creating required tables
├── Bank Management System FlowChart.pdf  # Visual representation of system workflow
├── **pycache**/             # Compiled Python cache files
└── README.md                # Project documentation

````

---

## 🚀 Getting Started

### 🧩 Prerequisites

Make sure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/)

Install the MySQL connector:
```bash
pip install mysql-connector-python
````


### ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/BANKING-MANAGEMENT-SYSTEM.git
```

Navigate to the project directory:

```bash
cd "BANKING MANAGEMENT SYSTEM"
```

---

### ▶️ Usage

1. **Run the main program:**

   ```bash
   python main.py
   ```

2. **Choose from the available options:**

   ```
   1. Sign Up
   2. Sign In
   ```

3. **After Sign In, you can:**

   * Check balance
   * Deposit / Withdraw money
   * Transfer funds to another account
   * View your transaction history
   * Exit securely

---

## 🧠 Code Overview

* **main.py:** Controls the main user interface and menu.
* **register.py:** Manages user registration and account creation.
* **bank.py:** Handles deposits, withdrawals, fund transfers, and transaction recording.
* **database.py:** Defines the `db_query()` function for database operations.
* **customer.py:** Contains the `Customer` class structure.
* **bnksysmgmt.sql:** Contains all SQL scripts required for database creation.

---

## 🔮 Future Enhancements

* Add admin panel for monitoring users and transactions.
* Implement account locking after multiple failed login attempts.
* Add GUI (Tkinter or Flask web interface).
* Email/SMS alerts for each transaction.
* Enhanced password encryption and authentication system.

---

## 🤝 Contributing

We welcome contributions to make this project better.
Feel free to fork the repository, create a new branch, make your changes, and submit a pull request.

---

## 📬 Contact

**Developer:** [Mohammed Habeebuddin](https://www.linkedin.com/in/mohammed-habeebuddin)

💼 *Backend Developer | Python | Django | MySQL | Cybersecurity Enthusiast*

---

**📘 Repository Link:**
[GitHub: Banking Management System](https://github.com/your-username/BANKING-MANAGEMENT-SYSTEM)

```
