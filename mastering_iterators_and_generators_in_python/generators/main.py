import random

def dice_roller():
    while True:
        yield random.randint(1, 6)

# Step 1: Create a generator
dice_generator = dice_roller()

# Step 2: Roll the die using the generator
for i, roll in enumerate(dice_generator):
    if i >= 10:  # Stop after 10 rolls
        break
    print(f"Rolled: {roll}")