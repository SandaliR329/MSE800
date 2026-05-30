# Parent class
# This parent "Flight" class represents a general flight
class Flight:
    def __init__(self, flight_number, airline_name, departure_city, arrival_city, departure_time):
        # declare Common attributes for all flights
        self.flight_number = flight_number
        self.airline_name = airline_name
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time

    # Common method inherited by subclasses
    def display_flight_info(self):
        print("Flight Information")
        print("------------------")
        print(f"Flight Number: {self.flight_number}")
        print(f"Airline Name: {self.airline_name}")
        print(f"Departure City: {self.departure_city}")
        print(f"Arrival City: {self.arrival_city}")
        print(f"Departure Time: {self.departure_time}")

    # Common method to update departure time
    def update_departure_time(self, new_time):
        self.departure_time = new_time
        print(f"Departure time updated to {self.departure_time}")


# Subclass
# DomesticFlight inherits attributes and methods from Flight
class DomesticFlight(Flight):
    def __init__(self, flight_number, airline_name, departure_city, arrival_city,
                 departure_time, terminal_number, baggage_allowance):

        # Calling parent class constructor using super()
        super().__init__(flight_number, airline_name, departure_city, arrival_city, departure_time)

        # Attributes specific to domestic flights
        self.terminal_number = terminal_number
        self.baggage_allowance = baggage_allowance

    # Method specific to DomesticFlight
    def display_domestic_info(self):
        # Reusing inherited method from parent class
        self.display_flight_info()

        print("\nDomestic Flight Details")
        print("-----------------------")
        print(f"Terminal Number: {self.terminal_number}")
        print(f"Baggage Allowance: {self.baggage_allowance} kg")


# Main program
# Creating an object of DomesticFlight class
domestic_flight = DomesticFlight(
    "NZ501",
    "Air New Zealand",
    "Auckland",
    "Wellington",
    "08:30 AM",
    "Domestic Terminal 1",
    23
)

# Calling subclass method
domestic_flight.display_domestic_info()

print()

# Calling inherited method from parent class
domestic_flight.update_departure_time("09:00 AM")

print()

# Display updated flight details
domestic_flight.display_domestic_info()