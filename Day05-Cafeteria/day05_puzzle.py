
print("Day 5 - Cafeteria")

# Puzzle I:
# Given is a list of numbers and a list of ranges.
# We need to check for each number if it is covered by any range.
#
# We read the ranges and the numbers.
# We sort the input and pick the first range.
# Then we check each number, until we pick a number that
# exceeds the range. We proceed with the next range then.
#


class Interval:
    def __init__(self, data:str=None, start:int=None, end:int=None):
        if not data == None:
            return self.init_from_string(data)

        if not start == None and not end == None:
            return self.init_from_ints(start, end)

    def init_from_string(self, data:str):
        tokens = data.split("-")
        self.start = int(tokens[0])
        self.end = int(tokens[1])
        assert self.start <= self.end, "Damn Elves - The start of an interval must be smaller or equal to the end."

    def init_from_ints(self, start:int, end:int):
        self.start = start
        self.end = end
        assert self.start <= self.end, "Damn Elves - The start of an interval must be smaller or equal to the end."

    def __lt__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        if (self.start < other.start):
            return True
        if (self.start == other.start):
            return (self.end < other.end)
        return False

    def __eq__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        return (self.start == other.start) and (self.end == other.end)

    def __str__(self):
        return "(" + str(self.start) + " - " + str(self.end) + ")"

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def contains(self, value):
        return self.start <= value and value <= self.end

    def size(self):
        return self.end - self.start + 1


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
file = open("input.data", "r")
# file = open("example.data", "r")
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