from domestic_flight import DomesticFlight
from international_flight import InternationalFlight
from regional_flight import RegionalFlight
from long_haul_international_flight import LongHaulInternationalFlight


def main():
    print("===== Air New Zealand Flight Management System =====")

    domestic_flight = DomesticFlight(
        "NZ501",
        "Air New Zealand",
        "Auckland",
        "Wellington",
        "08:30 AM",
        "D1",
        23
    )

    international_flight = InternationalFlight(
        "NZ101",
        "Air New Zealand",
        "Auckland",
        "Sydney",
        "10:00 AM",
        True,
        True
    )

    regional_flight = RegionalFlight(
        "NZ701",
        "Air New Zealand",
        "Auckland",
        "Rotorua",
        "07:15 AM",
        "D2",
        20,
        "Bay of Plenty",
        True
    )

    long_haul_flight = LongHaulInternationalFlight(
        "NZ005",
        "Air New Zealand",
        "Auckland",
        "Los Angeles",
        "09:45 PM",
        True,
        True,
        True,
        10
    )

    domestic_flight.display_info()
    domestic_flight.check_terminal()
    domestic_flight.calculate_price(120)

    international_flight.display_info()
    international_flight.check_documents()
    international_flight.calculate_price(500)

    regional_flight.display_info()
    regional_flight.check_region()
    regional_flight.calculate_price(90)

    long_haul_flight.display_info()
    long_haul_flight.check_landing_type()
    long_haul_flight.calculate_price(900)

    print("\n--- Demonstrating inherited parent methods ---")
    domestic_flight.update_time("09:00 AM")
    regional_flight.calculate_duration(1)
    long_haul_flight.calculate_duration(12)


if __name__ == "__main__":
    main()