# Login & Signup System

## Project Overview

This project is a Python-based Login and Signup System developed using Object-Oriented Programming principles. It allows users to create an account, sign in using a username and password, view profile details, and reset forgotten passwords.

The system uses SQLite as the database and BCrypt for secure password hashing.

## Features

- User signup
- User login using username and password
- Forgot password functionality
- User profile display
- SQLite database storage
- BCrypt password hashing
- Username uniqueness validation
- Password confirmation validation

## User Details Stored

- Full Name
- Date of Birth
- Username
- Hashed Password

## Technologies Used

| Technology | Purpose |
|----------|---------|
| Python | Main programming language |
| SQLite | Database |
| BCrypt | Password hashing |
| OOP | Project structure and maintainability |

## Project Structure

```text
login_signup_system/
├── main.py
├── database.py
├── user.py
├── auth_service.py
├── user_service.py
└── README.md