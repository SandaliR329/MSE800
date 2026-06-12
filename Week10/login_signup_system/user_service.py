import sqlite3
from database import Database
from user import User
from auth_service import AuthService


class UserService:
    def __init__(self):
        self.database = Database()

    def signup(self, full_name, date_of_birth, email, password):
        password_hash = AuthService.hash_password(password)
        user = User(full_name, date_of_birth, email, password_hash)

        try:
            with self.database.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users 
                    (full_name, date_of_birth, email, password_hash)
                    VALUES (?, ?, ?, ?)
                """, (
                    user.full_name,
                    user.date_of_birth,
                    user.email,
                    user.password_hash
                ))
                conn.commit()

            print("Signup successful!")

        except sqlite3.IntegrityError:
            print("Email already exists.")

    def login(self, email, password):
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT full_name, date_of_birth, email, password_hash
                FROM users
                WHERE email = ?
            """, (email,))

            user = cursor.fetchone()

        if user is None:
            print("User not found.")
            return

        stored_hash = user[3]

        if AuthService.verify_password(password, stored_hash):
            print("Login successful!")
            self.display_profile(user)
        else:
            print("Incorrect password.")

    def forgot_password(self, email, new_password):
        new_password_hash = AuthService.hash_password(new_password)

        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE users
                SET password_hash = ?
                WHERE email = ?
            """, (new_password_hash, email))
            conn.commit()

            if cursor.rowcount > 0:
                print("Password reset successful!")
            else:
                print("Email not found.")

    def display_profile(self, user):
        print("\n--- User Profile ---")
        print("Full Name:", user[0])
        print("Date of Birth:", user[1])
        print("Email:", user[2])