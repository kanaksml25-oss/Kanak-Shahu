import random

history = []

def roll_dice(num_dice):
    results = []
    for i in range(num_dice):
        number = random.randint(1, 6)
        results.append(number)
        history.append(number)
    return results

def show_history():
    if len(history) == 0:
        print("No rolls yet.")
    else:
        print("Roll history:", history)

def show_statistics():
    if len(history) == 0:
        print("No rolls yet, so no statistics.")
        return
    print("Total rolls:", len(history))
    print("Highest roll:", max(history))
    print("Lowest roll:", min(history))
    print("Average roll:", round(sum(history) / len(history), 2))
    print("\nHow many times each number appeared:")
    for face in range(1, 7):
        count = history.count(face)
        print(face, ":", count, "times")

def clear_history():
    history.clear()
    print("History cleared.")

while True:
    print("\n1. Roll Dice")
    print("2. View History")
    print("3. View Statistics")
    print("4. Clear History")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            num = int(input("How many dice do you want to roll? "))
            if num <= 0:
                print("Please enter a number greater than 0.")
            else:
                results = roll_dice(num)
                print("You rolled:", results)

        elif choice == 2:
            show_history()

        elif choice == 3:
            show_statistics()

        elif choice == 4:
            clear_history()

        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    except ValueError:
        print("Please enter a valid number.")