import random

# Create empty history list
history = []

while True:
    # Show menu
    print("\n--- Dice Rolling Menu ---")
    print("1. Roll Dice")
    print("2. View History")
    print("3. Exit")

    # Get user's choice
    choice = input("Enter your choice: ")

    # Choice 1: Roll Dice
    if choice == "1":
        number = random.randint(1, 6)

        print("You rolled:", number)

        # Add number to history
        history.append(number)

    # Choice 2: View History
    elif choice == "2":
        if len(history) == 0:
            print("No rolls yet.")
        else:
            print("Roll History:", history)

    # Choice 3: Exit
    elif choice == "3":
        print("Thank you!")
        break

    # Wrong input
    else:
        print("Invalid choice! Please enter 1, 2 or 3.")