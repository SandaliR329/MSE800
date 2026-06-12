from user_service import UserService


def main():
    user_service = UserService()

    while True:
        print("\n--- Login & Signup System ---")
        print("1. Signup")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            full_name = input("Enter full name: ")
            date_of_birth = input("Enter date of birth: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            confirm_password = input("Confirm password: ")

            if password == confirm_password:
                user_service.signup(full_name, date_of_birth, username, password)
            else:
                print("Passwords do not match.")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_service.login(username, password)

        elif choice == "3":
            username = input("Enter username: ")
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm new password: ")

            if new_password == confirm_password:
                user_service.forgot_password(username, new_password)
            else:
                print("Passwords do not match.")

        elif choice == "4":
            print("System closed.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()