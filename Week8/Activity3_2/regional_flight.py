from domestic_flight import DomesticFlight


class RegionalFlight(DomesticFlight):
    def __init__(self, flight_no, airline, departure_city,
                 arrival_city, departure_time, terminal_no,
                 baggage_limit, region_name, small_airport):
        super().__init__(
            flight_no,
            airline,
            departure_city,
            arrival_city,
            departure_time,
            terminal_no,
            baggage_limit
        )

        self.region_name = region_name
        self.small_airport = small_airport

    def display_info(self):
        super().display_info()
        print("Flight Category : Regional")
        print(f"Region Name     : {self.region_name}")
        print(f"Small Airport   : {self.small_airport}")

    def check_region(self):
        print(f"This flight operates within the {self.region_name} region.")

    def calculate_price(self, base_price):
        final_price = base_price + 20
        print(f"Regional flight ticket price: ${final_price}")