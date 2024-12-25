while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Get user input for operation choice
    choice = input("Choose an operation (1-5): ")

    if choice == "5":
        print("Exiting the calculator.")
        break  # Exit the program

    # Check if the choice is valid
    if choice in ["1", "2", "3", "4"]:
        try:
            # Get numbers from the user
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))

            # Perform the chosen operation
            if choice == "1":
                print("Result:", number1 + number2)
            elif choice == "2":
                print("Result:", number1 - number2)
            elif choice == "3":
                print("Result:", number1 * number2)
            elif choice == "4":
                if number2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print("Result:", number1 / number2)
        except ValueError:
            print("Invalid input! Please enter a number.")
    else:
        print("Invalid choice, please enter a value between 1-5.")
