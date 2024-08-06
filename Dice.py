import random

def roll_dice(num_dice=1, sides=6):
    """Simulates rolling `num_dice` dice, each with `sides` sides."""
    results = [random.randint(1, sides) for _ in range(num_dice)]
    return results

def main():
    print("Welcome to the Dice Simulator!")
    
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (or 0 to quit): "))
            if num_dice == 0:
                print("Thanks for playing!")
                break
            if num_dice < 0:
                print("Number of dice cannot be negative. Please enter a positive number.")
                continue

            sides = int(input("Enter the number of sides on each die: "))
            if sides < 2:
                print("A die must have at least 2 sides. Please enter a valid number of sides.")
                continue

            results = roll_dice(num_dice, sides)
            print(f"Rolling {num_dice} dice with {sides} sides each:")
            print("Results:", results)
            print("Total:", sum(results))

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
