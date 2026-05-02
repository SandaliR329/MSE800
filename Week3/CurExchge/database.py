import sqlite3

def create_connection():
    conn = sqlite3.connect("exchange.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            cus_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone INTEGER NOT NULL,
            address TEXT NOT NULL,
            dob TEXT NOT NULL
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_type TEXT NOT NULL,
        balance REAL NOT NULL,
        status TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_account (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cus_id INTEGER NOT NULL,
        account_id INTEGER NOT NULL,
        role TEXT,
        created_date TEXT,
        status TEXT,
        FOREIGN KEY (cus_id) REFERENCES customers(cus_id),
        FOREIGN KEY (account_id) REFERENCES accounts(account_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS currency (
        currency_code TEXT PRIMARY KEY,
        symbol TEXT,
        buying_rate REAL,
        selling_rate REAL,
        country TEXT,
        description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        type TEXT NOT NULL,
        date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (account_id) REFERENCES accounts(account_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exchange (
        exchange_id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_id INTEGER NOT NULL,
        from_currency TEXT NOT NULL,
        to_currency TEXT NOT NULL,
        exchange_rate REAL,
        converted_amount REAL,
        FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id),
        FOREIGN KEY (from_currency) REFERENCES currency(currency_code),
        FOREIGN KEY (to_currency) REFERENCES currency(currency_code)
    )
    ''')
    conn.commit()
    conn.close()






