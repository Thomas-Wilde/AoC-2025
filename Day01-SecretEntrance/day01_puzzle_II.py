
print("Day 1 - SecretEntrance")

# Using readlines()
# file = open("input.data", "r")
file = open("example.data", "r")
lines = file.readlines()

dial = 50
zero_count = 0

for l in lines:
    clicks = int(l[1:])
    change = 1
    if l[0] == "L":
        change = -change
    for i in range(clicks):
      dial += change
      dial = dial%100
      if (dial == 0):
          zero_count += 1

print("--- result ---")
print(zero_count)