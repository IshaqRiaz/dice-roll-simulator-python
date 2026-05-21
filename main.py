import random

again = True
count = 0  # Counter to track number of rolls

while again:

    try:
        num = int(input("How many dice do you want to roll?: "))

        if num <= 0:
            print("Please enter a number greater than 0.\n")
            continue

    except ValueError:
        print("Invalid input! Please enter a number.\n")
        continue

    print("Rolling dice...\n")

    for i in range(num):
        print(f"Dice {i+1}: {random.randint(1, 6)}")

    count += 1

    another_roll = input("\nDo you want to roll dice again? (y/n): ")

    if another_roll.lower() == "y":
        continue
    else:
        print("\nYou are quitting the game. Game Closed!")
        print("Total times you rolled the dice:", count)
        break
