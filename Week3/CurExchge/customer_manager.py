from database import create_connection
import sqlite3


# ➕ Add Customer
def add_customer(name, email, phone, address, dob):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO customers (name, email, phone, address, dob)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, address, dob))

        conn.commit()
        print("✅ Customer added successfully.")

    except sqlite3.IntegrityError:
        print("❌ Email must be unique.")

    conn.close()


# 📄 View All Customers
def view_customers():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    conn.close()
    return rows


# 🔍 Search Customer by Name
def search_customer(name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM customers
        WHERE name LIKE ?
    """, ('%' + name + '%',))

    rows = cursor.fetchall()
    conn.close()
    return rows


# 🔍 Search Customer by Email
def search_customer_by_email(email):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM customers
        WHERE email = ?
    """, (email,))

    row = cursor.fetchone()
    conn.close()
    return row


# ✏️ Update Customer
def update_customer(cus_id, name, email, phone, address, dob):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE customers
            SET name = ?, email = ?, phone = ?, address = ?, dob = ?
            WHERE cus_id = ?
        """, (name, email, phone, address, dob, cus_id))

        conn.commit()
        print("✏️ Customer updated successfully.")

    except sqlite3.IntegrityError:
        print("❌ Email must be unique.")

    conn.close()


# 🗑️ Delete Customer
def delete_customer(cus_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM customers
        WHERE cus_id = ?
    """, (cus_id,))

    conn.commit()
    conn.close()

    print("🗑️ Customer deleted.")