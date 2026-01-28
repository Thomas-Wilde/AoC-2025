
print("Day 6 - Trash Compactor")

def read_input(data, intervals, numbers):
    for line in data:
        line = line.strip()
        if len(line) == 0:
            continue
        idx = line.find("-")
        if not idx == -1:
            intervals.append(Interval(data=str(line)))
            continue
        else:
            numbers.append(int(line))

def count_fresh_numbers(intervals, numbers):
    fresh_count = 0
    for number in numbers:
        for interval in intervals:
            if interval.contains(number):
                fresh_count += 1
                break
    return fresh_count

def create_canoncial_intervals(intervals):
    intervals.sort()
    canon = []
    canon.append(intervals.pop(0))
    while len(intervals) > 0:
        interval_0 = canon.pop()
        interval_1 = intervals.pop(0)

        if interval_0.get_end() >= interval_1.get_start():
            start = interval_0.get_start()
            end = max(interval_0.get_end(), interval_1.get_end())
            canon.append(Interval(start=start, end=end))
            continue
        canon.append(interval_0)
        canon.append(interval_1)
    return canon

def count_total_fresh_numbers(intervals):
    total = 0
    for interval in intervals:
        total += interval.size()
    return total

# --- main ---
# read data
# file = open("input.data", "r")
file = open("example.data", "r")
data = file.readlines()
intervals = []
numbers = []

read_input(data, intervals, numbers)

for i in intervals:
     print(i)
print("---")

intervals = create_canoncial_intervals(intervals)
numbers.sort()

for i in intervals:
     print(i)

for i in numbers:
     print(i)

fresh_count = count_fresh_numbers(intervals, numbers)
total_fresh_count = count_total_fresh_numbers(intervals)

print("--- result: count of fresh items ---")
print(fresh_count)
print("--- result: total count of fresh items ---")
print(total_fresh_count)