from abc import ABC, abstractmethod
import uuid


# =====================================
# 1. FLIGHT CLASS
# =====================================

class Flight:

    def __init__(self, flight_code, airline, source,
                 destination, seats, base_fare):

        self.__flight_code = flight_code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__available_seats = seats
        self.__base_fare = base_fare

    @property
    def flight_code(self):
        return self.__flight_code

    @property
    def airline(self):
        return self.__airline

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def available_seats(self):
        return self.__available_seats

    @property
    def base_fare(self):
        return self.__base_fare

    def book_seats(self, count):

        if count <= self.__available_seats:
            self.__available_seats -= count
            return True

        return False

    def display_flight(self):

        print("------------------------------------------")
        print("Flight Code :", self.flight_code)
        print("Airline     :", self.airline)
        print("Source      :", self.source)
        print("Destination :", self.destination)
        print("Seats       :", self.available_seats)
        print("Base Fare   : Rs.", self.base_fare)


# =====================================
# 2. ABSTRACT PASSENGER CLASS
# =====================================

class Passenger(ABC):

    def __init__(self, name, age):

        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass

    def calculate_fare(self, base_fare, tickets):

        total = base_fare * tickets

        discount = total * self.get_discount() / 100

        final_amount = total - discount

        return total, discount, final_amount


# =====================================
# 3. REGULAR PASSENGER
# =====================================

class RegularPassenger(Passenger):

    def get_discount(self):

        return 5


# =====================================
# 4. STUDENT PASSENGER
# =====================================

class StudentPassenger(Passenger):

    def get_discount(self):

        return 15


# =====================================
# 5. BOOKING CLASS
# =====================================

class Booking:

    def __init__(self, passenger, flight,
                 tickets, base_fare, discount,
                 final_amount):

        self.booking_id = "BK" + str(uuid.uuid4())[:8].upper()

        self.passenger = passenger
        self.flight = flight
        self.tickets = tickets
        self.base_fare = base_fare
        self.discount = discount
        self.final_amount = final_amount

    def display_booking(self):

        print("\n========== BOOKING SUMMARY ==========")

        print("Booking ID      :", self.booking_id)

        print("Passenger Name  :", self.passenger.name)

        print("Passenger Age   :", self.passenger.age)

        print("Flight Code     :", self.flight.flight_code)

        print("Airline         :", self.flight.airline)

        print("Source          :", self.flight.source)

        print("Destination     :", self.flight.destination)

        print("Number of Tickets:", self.tickets)

        print("Base Fare       : Rs.", self.base_fare)

        print("Discount        : Rs.", self.discount)

        print("Final Amount    : Rs.", self.final_amount)

        print("=====================================")

        print("Booking Confirmed Successfully!")


# =====================================
# 6. FLIGHT BOOKING SYSTEM
# =====================================

class FlightBookingSystem:

    def __init__(self):

        self.flights = [

            Flight("F101", "IndiGo", "Pune",
                   "Mumbai", 50, 2500),

            Flight("F102", "Air India", "Pune",
                   "Delhi", 40, 5500),

            Flight("F103", "SpiceJet", "Mumbai",
                   "Bangalore", 35, 4500),

            Flight("F104", "Vistara", "Delhi",
                   "Chennai", 30, 6000),

            Flight("F105", "IndiGo", "Mumbai",
                   "Goa", 45, 3000)

        ]

        self.last_booking = None

    # ---------------------------------
    # DISPLAY AVAILABLE FLIGHTS
    # ---------------------------------

    def view_flights(self):

        print("\n========== AVAILABLE FLIGHTS ==========")

        for flight in self.flights:

            flight.display_flight()

        print("------------------------------------------")

    # ---------------------------------
    # FIND FLIGHT BY CODE
    # ---------------------------------

    def find_flight(self, code):

        for flight in self.flights:

            if flight.flight_code.lower() == code.lower():

                return flight

        return None

    # ---------------------------------
    # INPUT VALIDATION
    # ---------------------------------

    def get_integer(self, message, minimum, maximum=None):

        while True:

            try:

                value = int(input(message))

                if value < minimum:

                    print("Please enter a valid value.")

                elif maximum is not None and value > maximum:

                    print("Value exceeds the allowed limit.")

                else:

                    return value

            except ValueError:

                print("Invalid input! Please enter a number.")

    # ---------------------------------
    # BOOK FLIGHT
    # ---------------------------------

    def book_flight(self):

        print("\n========== FLIGHT BOOKING ==========")

        code = input("Enter Flight Code: ").strip()

        flight = self.find_flight(code)

        if flight is None:

            print("Error: Flight not found!")

            return

        if flight.available_seats == 0:

            print("Sorry! No seats available.")

            return

        print("\nFlight Selected:", flight.flight_code)

        print("Airline:", flight.airline)

        print("Route:", flight.source, "to", flight.destination)

        print("Available Seats:", flight.available_seats)

        name = input("\nEnter Passenger Name: ").strip()

        if not name or not any(char.isalpha() for char in name):

            print("Invalid passenger name!")

            return

        age = self.get_integer(
            "Enter Passenger Age: ", 1, 120
        )

        tickets = self.get_integer(
            "Enter Number of Tickets: ",
            1,
            flight.available_seats
        )

        print("\nSelect Passenger Category:")

        print("1. Regular Passenger (5% Discount)")

        print("2. Student Passenger (15% Discount)")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            passenger = RegularPassenger(name, age)

        elif choice == "2":

            passenger = StudentPassenger(name, age)

        else:

            print("Invalid passenger category!")

            return

        # Calculate fare using polymorphism

        total, discount, final_amount = passenger.calculate_fare(
            flight.base_fare, tickets
        )

        print("\n========== FARE DETAILS ==========")

        print("Total Base Fare : Rs.", total)

        print("Discount        : Rs.", discount)

        print("Final Amount    : Rs.", final_amount)

        confirm = input("\nConfirm Booking? (yes/no): ").strip().lower()

        if confirm != "yes":

            print("Booking Cancelled!")

            return

        # Update seats only after confirmation

        if not flight.book_seats(tickets):

            print("Booking failed! Seats are not available.")

            return

        # Create booking object

        booking = Booking(
            passenger,
            flight,
            tickets,
            total,
            discount,
            final_amount
        )

        self.last_booking = booking

        # Display booking summary

        booking.display_booking()

    # ---------------------------------
    # CALCULATE FARE
    # ---------------------------------

    def calculate_fare(self):

        print("\n========== FARE CALCULATION ==========")

        code = input("Enter Flight Code: ").strip()

        flight = self.find_flight(code)

        if flight is None:

            print("Flight not found!")

            return

        print("1. Regular Passenger (5% Discount)")

        print("2. Student Passenger (15% Discount)")

        choice = input("Select Passenger Category: ").strip()

        if choice == "1":

            passenger = RegularPassenger("Guest", 18)

        elif choice == "2":

            passenger = StudentPassenger("Guest", 18)

        else:

            print("Invalid choice!")

            return

        tickets = self.get_integer(
            "Enter Number of Tickets: ",
            1,
            flight.available_seats
        )

        total, discount, final_amount = passenger.calculate_fare(
            flight.base_fare, tickets
        )

        print("\nBase Fare      : Rs.", total)

        print("Discount       : Rs.", discount)

        print("Final Fare     : Rs.", final_amount)

        print("\nNote: This is only a fare estimate.")

    # ---------------------------------
    # VIEW LAST BOOKING
    # ---------------------------------

    def view_booking(self):

        print("\n========== LAST BOOKING ==========")

        if self.last_booking is None:

            print("No confirmed booking found!")

        else:

            self.last_booking.display_booking()

    # ---------------------------------
    # MAIN MENU
    # ---------------------------------

    def run(self):

        print("\n======================================")

        print("       FLIGHT BOOKING SYSTEM")

        print("======================================")

        while True:

            print("\n========== MAIN MENU ==========")

            print("1. View Flights")

            print("2. Book Flight")

            print("3. Calculate Fare")

            print("4. View Booking")

            print("5. Exit")

            choice = input("\nEnter Your Choice: ").strip()

            if choice == "1":

                self.view_flights()

            elif choice == "2":

                self.book_flight()

            elif choice == "3":

                self.calculate_fare()

            elif choice == "4":

                self.view_booking()

            elif choice == "5":

                print("\nThank you for using Flight Booking System!")

                print("Have a safe journey!")

                break

            else:

                print("Invalid choice! Please select 1 to 5.")


# =====================================
# 7. MAIN PROGRAM
# =====================================

if __name__ == "__main__":

    system = FlightBookingSystem()

    system.run()