from international_flight import InternationalFlight


class LongHaulInternationalFlight(InternationalFlight):
    def __init__(self, flight_no, airline, departure_city,
                 arrival_city, departure_time, passport_required,
                 visa_required, lounge_access, extra_baggage):
        super().__init__(
            flight_no,
            airline,
            departure_city,
            arrival_city,
            departure_time,
            passport_required,
            visa_required
        )

        self.lounge_access = lounge_access
        self.extra_baggage = extra_baggage

    def display_info(self):
        super().display_info()
        print("Flight Category : Long-Haul International")
        print(f"Lounge Access   : {self.lounge_access}")
        print(f"Extra Baggage   : {self.extra_baggage} kg")

    def check_landing_type(self):
        print("This long-haul flight requires international arrival clearance.")

    def calculate_price(self, base_price):
        final_price = base_price + 300
        print(f"Long-haul international ticket price: ${final_price}")