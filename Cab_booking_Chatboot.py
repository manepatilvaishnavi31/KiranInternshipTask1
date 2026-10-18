import random

# Cab rates per kilometer
CAB_RATES = {
    1: ("Auto", 12),
    2: ("Sedan", 18),
    3: ("SUV", 25)
}

# All locations
locations = [
    "Pune Station",
    "Swargate",
    "Hinjawadi",
    "Shivajinagar",
    "Kothrud",
    "Wakad"
]

# Routes between every source and destination.
# Distances are sample distances for this assignment.
routes = {
    "Pune Station": {
        "Swargate": 7,
        "Hinjawadi": 20,
        "Shivajinagar": 5,
        "Kothrud": 12,
        "Wakad": 18
    },

    "Swargate": {
        "Pune Station": 7,
        "Hinjawadi": 22,
        "Shivajinagar": 6,
        "Kothrud": 10,
        "Wakad": 20
    },

    "Hinjawadi": {
        "Pune Station": 20,
        "Swargate": 22,
        "Shivajinagar": 15,
        "Kothrud": 12,
        "Wakad": 10
    },

    "Shivajinagar": {
        "Pune Station": 5,
        "Swargate": 6,
        "Hinjawadi": 15,
        "Kothrud": 8,
        "Wakad": 13
    },

    "Kothrud": {
        "Pune Station": 12,
        "Swargate": 10,
        "Hinjawadi": 12,
        "Shivajinagar": 8,
        "Wakad": 9
    },

    "Wakad": {
        "Pune Station": 18,
        "Swargate": 20,
        "Hinjawadi": 10,
        "Shivajinagar": 13,
        "Kothrud": 9
    }
}


def display_menu():
    print("\n========== CAB BOOKING CHATBOT ==========")
    print("1. Book Ride")
    print("2. Exit")


def choose_cab():
    print("\n---------- SELECT CAB TYPE ----------")
    print("1. Auto  - Rs. 12/km")
    print("2. Sedan - Rs. 18/km")
    print("3. SUV   - Rs. 25/km")

    while True:
        try:
            choice = int(input("Choose cab type (1-3): "))

            if choice in CAB_RATES:
                return CAB_RATES[choice]

            print("Invalid choice! Please select 1, 2, or 3.")

        except ValueError:
            print("Please enter a valid number.")


def display_locations():
    print("\n---------- AVAILABLE LOCATIONS ----------")

    for index, location in enumerate(locations, start=1):
        print(f"{index}. {location}")


def choose_location(message, excluded_location=None):
    while True:
        display_locations()

        try:
            choice = int(input(message))

            if choice < 1 or choice > len(locations):
                print("Invalid location number!")
                continue

            selected_location = locations[choice - 1]

            if selected_location == excluded_location:
                print("Source and destination cannot be the same!")
                continue

            return selected_location

        except ValueError:
            print("Please enter a valid number.")


def display_routes(source):
    print(f"\nAvailable destinations from {source}:")

    for destination, distance in routes[source].items():
        print(f"{destination} - {distance} km")


def book_ride():
    # Step 1: Choose cab
    cab_name, rate = choose_cab()

    # Step 2: Choose source
    source = choose_location("Choose source location number: ")

    # Step 3: Show all destinations from the source
    display_routes(source)

    # Step 4: Choose destination
    destination = choose_location(
        "Choose destination location number: ",
        excluded_location=source
    )

    # Step 5: Get the predefined route distance
    distance = routes[source][destination]

    # Step 6: Calculate fare
    fare = distance * rate

    print("\n========== BOOKING DETAILS ==========")
    print(f"Source      : {source}")
    print(f"Destination : {destination}")
    print(f"Cab Type    : {cab_name}")
    print(f"Distance    : {distance} km")
    print(f"Rate        : Rs. {rate}/km")
    print(f"Total Fare  : Rs. {fare}")

    # Step 7: Confirm or cancel before OTP
    while True:
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                break

            elif choice == 2:
                print("\nBooking cancelled successfully.")
                print("No OTP has been generated or shared.")
                return

            else:
                print("Invalid choice! Please enter 1 or 2.")

        except ValueError:
            print("Please enter a valid number.")

    # Step 8: Generate a four-digit OTP after confirmation
    otp = random.randint(1000, 9999)

    print("\n========== BOOKING CONFIRMED ==========")
    print("Your cab booking is confirmed!")
    print(f"Your OTP is: {otp}")
    print("Share this OTP with the driver to start your ride.")

    # Step 9: Cancellation is locked after OTP sharing
    print("\nIMPORTANT:")
    print("Your ride cannot be cancelled after OTP sharing.")

    print("\nThank you for using Cab Booking Chatbot!")


# Main program
while True:
    display_menu()

    try:
        main_choice = int(input("Enter your choice: "))

        if main_choice == 1:
            book_ride()

        elif main_choice == 2:
            print("\nThank you for using Cab Booking Chatbot!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1 or 2.")

    except ValueError:
        print("Invalid input! Please enter a number.")