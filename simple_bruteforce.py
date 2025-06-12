import random
from itertools import permutations
#UPDATE THE "n" WITH NUMBERS RANGING BETWEEN 11TO 9
# ANDROID PATTERN GRID: 
"'123
  456
  789"'
#IF U REMEMBER YOUR PASSWORD. U CAN CHECK IT WITH HOW MANY ATTEMPTS IT CAN CRACK YOUR PASSWORD BUT MAKE SURE TO UPDATE THE  "n" VALUES


# Define the Android 3x3 grid (dots 1 to 9)
dots = list(range(1, 10))

# Your real n-dot pattern (1 to 9) for simple android pattern
your_pattern = [] #put it here before executing

# Generate all 5-dot permutations (without repetition)
all_n_dot_patterns = list(permutations(dots, n))
total_patterns = len(all_n_dot_patterns)

# Shuffle to simulate random guessing
random.shuffle(all_n_dot_patterns)

# Brute-force attempt counter
attempts = 0
for pattern in all_n_dot_patterns:
    attempts += 1
    if list(pattern) == your_pattern:
        print(f" Pattern matched on attempt {attempts}!")
        break

print(f"Total n-dot patterns: {total_patterns}")
print(f"Your pattern: {your_pattern}")
print(f"Random guess matched in: {attempts} attempts")
