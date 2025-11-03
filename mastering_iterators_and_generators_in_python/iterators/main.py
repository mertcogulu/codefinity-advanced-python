import random

class InfiniteDie:
    def __iter__(self):
        return self

    def __next__(self):
        return random.randint(1, 6)

# Step 1: Create an infinite die iterator
infinite_die = InfiniteDie()

# Step 2: Roll the die lazily
for i, roll in enumerate(infinite_die):
    if i >= 10:  # Stop after 10 rolls
        break
    print(f"Rolled: {roll}")