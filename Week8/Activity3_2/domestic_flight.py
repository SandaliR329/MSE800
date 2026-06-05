from flight import Flight


class DomesticFlight(Flight):
    def __init__(self, flight_no, airline, departure_city,
                 arrival_city, departure_time, terminal_no,
                 baggage_limit):
        super().__init__(
            flight_no,
            airline,
            departure_city,
            arrival_city,
            departure_time
        )

        self.terminal_no = terminal_no
        self.baggage_limit = baggage_limit

    def display_info(self):
        super().display_info()
        print("Flight Type    : Domestic")
        print(f"Terminal No    : {self.terminal_no}")
        print(f"Baggage Limit  : {self.baggage_limit} kg")

    def check_terminal(self):
        print(f"Please proceed to domestic terminal {self.terminal_no}.")

    def calculate_price(self, base_price):
        final_price = base_price + 30
        print(f"Domestic flight ticket price: ${final_price}")