class Flight:
    def __init__(self, flight_no, airline, departure_city,
                 arrival_city, departure_time):
        self.flight_no = flight_no
        self.airline = airline
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time

    def display_info(self):
        print("\n--- Flight Information ---")
        print(f"Flight No      : {self.flight_no}")
        print(f"Airline        : {self.airline}")
        print(f"Departure City : {self.departure_city}")
        print(f"Arrival City   : {self.arrival_city}")
        print(f"Departure Time : {self.departure_time}")

    def update_time(self, new_time):
        self.departure_time = new_time
        print(f"Departure time updated to {self.departure_time}")

    def calculate_duration(self, hours):
        print(f"Estimated flight duration: {hours} hours")