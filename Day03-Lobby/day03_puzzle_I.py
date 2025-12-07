
print("Day 3 - Lobby")

# Puzzle I:
# Find the largest number that can be formed by 2 digits.
# The digits cannot be rearranged.
# Step 1:
# Go from left to right and find the largest digit - last postion is excluded.
# Step 2:
# Go from right to left and find the largest digit - first position is excluded.


def find_largest_left(joltage):
    digit_count = len(joltage)
    largest_left = -1
    largest_left_idx = -1
    for i in range(0, digit_count - 1):
        current_digit = int(joltage[i])
        if current_digit > largest_left:
            largest_left = current_digit
            largest_left_idx = i
    return largest_left, largest_left_idx

def find_largest_right(joltage, left_idx):
    digit_count = len(joltage)
    largest_right = -1
    largest_right_idx = -1
    for i in range(digit_count-1, left_idx, -1):
        current_digit = int(joltage[i])
        if current_digit > largest_right:
            largest_right = current_digit
            largest_right_idx = i
    return largest_right, largest_right_idx

# --- main ---
# read data
file = open("input.data", "r")
# file = open("example.data", "r")
data = file.readlines()

sum = 0
for row in data:
    joltage = row.strip()
    left, idx_left = find_largest_left(joltage)
    right, idx_right = find_largest_right(joltage, idx_left)

    jolts = left * 10 + right
    sum += jolts
    print(jolts)

print("--- result: total jolts ---")
print(sum)