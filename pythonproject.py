import random

def roll_dice(num_dice=1, num_sides=6):
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    return rolls

while True:
    try:
        num_dice = int(input("How many dice would you like to roll? "))
        num_sides = int(input("How many sides do the dice have? "))
        break
    except ValueError:
        print("Invalid input. Please enter integers for the number of dice and sides.")

results = roll_dice(num_dice, num_sides)

print("You rolled:", results)

total = sum(results)
print("Total:", total)
