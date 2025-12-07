
print("Day 3 - Lobby")

# Puzzle I:
# Find the largest number that can be formed by 12 digits.
# The digits cannot be rearranged.
# Idea:
# Go from left to right for each digit.
# Find the largest digit that leaves at least 12 more digits to the right.


def find_largest_digit(joltage, start_idx, end_idx):
    largest = -1
    largest_idx = -1
    for i in range(start_idx, end_idx, 1):
        current_digit = int(joltage[i])
        if current_digit > largest:
            largest = current_digit
            largest_idx = i
    return largest, largest_idx

def find_largest_joltage(joltage, battery_count):
    digit_count = len(joltage)
    remaining = battery_count
    start_idx = 0
    jolt_sum = 0
    while remaining > 0:
        remaining -= 1
        end_idx = digit_count - remaining
        largest, largest_idx = find_largest_digit(joltage, start_idx, end_idx)
        start_idx = largest_idx + 1
        jolt_sum = jolt_sum * 10 + largest
    return jolt_sum
# --- main ---
# read data
file = open("input.data", "r")
# file = open("example.data", "r")
data = file.readlines()

sum = 0
for row in data:
    joltage = row.strip()
    jolts = find_largest_joltage(joltage, 12)
    print(jolts)
    sum += jolts

print("--- result: total jolts ---")
print(sum)