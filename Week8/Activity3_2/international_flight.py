from flight import Flight


class InternationalFlight(Flight):
    def __init__(self, flight_no, airline, departure_city,
                 arrival_city, departure_time, passport_required,
                 visa_required):
        super().__init__(
            flight_no,
            airline,
            departure_city,
            arrival_city,
            departure_time
        )

        self.passport_required = passport_required
        self.visa_required = visa_required

    def display_info(self):
        super().display_info()
        print("Flight Type       : International")
        print(f"Passport Required : {self.passport_required}")
        print(f"Visa Required     : {self.visa_required}")

    def check_documents(self):
        if self.passport_required and self.visa_required:
            print("Passport and visa are required for this flight.")
        elif self.passport_required:
            print("Passport is required for this flight.")
        else:
            print("No special travel documents required.")

    def calculate_price(self, base_price):
        final_price = base_price + 150
        print(f"International flight ticket price: ${final_price}")