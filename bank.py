balance = 10000

print("Welcome to Kiran Bank")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Deposit successful.")
                print("Updated Balance: ₹", balance)
            else:
                print("Invalid amount. Enter an amount greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount. Enter an amount greater than 0.")

            elif amount > balance:
                print("Transaction failed: Insufficient balance.")
                print("Current Balance: ₹", balance)

            else:
                balance -= amount
                print("Withdrawal successful.")
                print("Updated Balance: ₹", balance)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")1