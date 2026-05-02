from land import Land


def main():
    print("=== Land Calculator ===")

    # User input
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    # Create object
    land = Land(length, width)

    # Output
    print("\n--- Results ---")
    land.print_dimensions()
    print(f"Area: {land.calculate_area()}")
    print(f"Perimeter: {land.calculate_perimeter()}")


if __name__ == "__main__":
    main()