# database.py
# Database Management Banking
import mysql.connector as sql

# Connect to the MySQL database
mydb = sql.connect(
    host="localhost",
    user="root",
    password="Qwerty@1234",   # update if changed
    database="bank"
)

cursor = mydb.cursor()

def db_query(query):
    """Execute a query and return results (if any)."""
    cursor.execute(query)
    try:
        result = cursor.fetchall()
        return result
    except:
        return None

def create_customers_table():
    """Ensure main customer table exists."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            username VARCHAR(20) NOT NULL UNIQUE,
            password VARCHAR(20) NOT NULL,
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            city VARCHAR(50) NOT NULL,
            balance INT DEFAULT 0,
            account_number BIGINT NOT NULL UNIQUE,
            status BOOLEAN NOT NULL DEFAULT 1
        );
    ''')
    mydb.commit()

# Auto-create table when run directly
if __name__ == "__main__":
    create_customers_table()
    print(" customers table ready.")
