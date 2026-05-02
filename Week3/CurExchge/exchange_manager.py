from database import create_connection
import sqlite3


# ➕ Add Exchange
def add_exchange(transaction_id, from_currency, to_currency, exchange_rate, converted_amount):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO exchange 
            (transaction_id, from_currency, to_currency, exchange_rate, converted_amount)
            VALUES (?, ?, ?, ?, ?)
        """, (transaction_id, from_currency, to_currency, exchange_rate, converted_amount))

        conn.commit()
        print("✅ Exchange added successfully.")

    except sqlite3.IntegrityError as e:
        print("❌ Error:", e)

    conn.close()


# 📄 View All Exchanges
def view_exchanges():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM exchange")
    rows = cursor.fetchall()

    conn.close()
    return rows


# 🔍 Search by Transaction ID
def search_exchange_by_transaction(transaction_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM exchange
        WHERE transaction_id = ?
    """, (transaction_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows


# 🔍 Search by Currency
def search_exchange_by_currency(currency_code):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM exchange
        WHERE from_currency = ? OR to_currency = ?
    """, (currency_code, currency_code))

    rows = cursor.fetchall()
    conn.close()
    return rows


# ✏️ Update Exchange Rate
def update_exchange_rate(exchange_id, new_rate):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE exchange
        SET exchange_rate = ?
        WHERE exchange_id = ?
    """, (new_rate, exchange_id))

    conn.commit()
    conn.close()

    print("✏️ Exchange rate updated.")


# 🗑️ Delete Exchange
def delete_exchange(exchange_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM exchange
        WHERE exchange_id = ?
    """, (exchange_id,))

    conn.commit()
    conn.close()

    print("🗑️ Exchange deleted.")


# 🔗 View Exchange with Customer Details (JOIN)
def view_exchange_with_customer():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            e.exchange_id,
            c.name,
            a.account_id,
            t.transaction_id,
            e.from_currency,
            e.to_currency,
            e.exchange_rate,
            e.converted_amount
        FROM exchange e
        JOIN transactions t ON e.transaction_id = t.transaction_id
        JOIN accounts a ON t.account_id = a.account_id
        JOIN customer_account ca ON a.account_id = ca.account_id
        JOIN customers c ON ca.cus_id = c.cus_id
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


# 🔍 Search Exchange by Customer Name
def search_exchange_by_customer(name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            e.exchange_id,
            c.name,
            e.from_currency,
            e.to_currency,
            e.exchange_rate,
            e.converted_amount
        FROM exchange e
        JOIN transactions t ON e.transaction_id = t.transaction_id
        JOIN accounts a ON t.account_id = a.account_id
        JOIN customer_account ca ON a.account_id = ca.account_id
        JOIN customers c ON ca.cus_id = c.cus_id
        WHERE c.name LIKE ?
    """, ('%' + name + '%',))

    rows = cursor.fetchall()
    conn.close()
    return rows