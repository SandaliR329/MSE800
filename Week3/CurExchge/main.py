from database import create_table

# Exchange functions
from exchange_manager import (
    add_exchange,
    view_exchanges,
    search_exchange_by_transaction,
    search_exchange_by_currency,
    update_exchange_rate,
    delete_exchange,
    view_exchange_with_customer,
    search_exchange_by_customer
)

# Customer functions
from customer_manager import (
    add_customer,
    view_customers,
    search_customer,
    delete_customer
)


def menu():
    print("\n========= MAIN MENU =========")

    print("\n--- Customer Management ---")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Delete Customer")

    print("\n--- Exchange Management ---")
    print("5. Add Exchange")
    print("6. View Exchanges")
    print("7. Search by Transaction ID")
    print("8. Search by Currency")
    print("9. Update Exchange Rate")
    print("10. Delete Exchange")
    print("11. View Exchange with Customer")
    print("12. Search Exchange by Customer")

    print("\n13. Exit")


def main():
    create_table()

    while True:
        menu()
        choice = input("Select an option (1-13): ")

        # ================= CUSTOMER =================

        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")

            add_customer(name, email, phone, address, dob)

        elif choice == '2':
            customers = view_customers()
            for c in customers:
                print(c)

        elif choice == '3':
            name = input("Enter name to search: ")
            results = search_customer(name)
            for r in results:
                print(r)

        elif choice == '4':
            cid = int(input("Enter Customer ID to delete: "))
            delete_customer(cid)

        # ================= EXCHANGE =================

        elif choice == '5':
            transaction_id = int(input("Transaction ID: "))
            from_currency = input("From Currency: ")
            to_currency = input("To Currency: ")
            exchange_rate = float(input("Exchange Rate: "))
            converted_amount = float(input("Converted Amount: "))

            add_exchange(transaction_id, from_currency, to_currency, exchange_rate, converted_amount)

        elif choice == '6':
            exchanges = view_exchanges()
            for e in exchanges:
                print(e)

        elif choice == '7':
            tid = int(input("Enter Transaction ID: "))
            results = search_exchange_by_transaction(tid)
            for r in results:
                print(r)

        elif choice == '8':
            currency = input("Enter Currency Code: ")
            results = search_exchange_by_currency(currency)
            for r in results:
                print(r)

        elif choice == '9':
            eid = int(input("Exchange ID: "))
            new_rate = float(input("New Rate: "))
            update_exchange_rate(eid, new_rate)

        elif choice == '10':
            eid = int(input("Exchange ID to delete: "))
            delete_exchange(eid)

        elif choice == '11':
            results = view_exchange_with_customer()
            for r in results:
                print(f"""
Exchange ID: {r[0]}
Customer: {r[1]}
Account ID: {r[2]}
Transaction ID: {r[3]}
From: {r[4]} → To: {r[5]}
Rate: {r[6]}
Amount: {r[7]}
---------------------------
""")

        elif choice == '12':
            name = input("Enter Customer Name: ")
            results = search_exchange_by_customer(name)
            for r in results:
                print(r)

        # ================= EXIT =================

        elif choice == '13':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()