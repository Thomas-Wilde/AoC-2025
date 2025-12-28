print("Day 6 - Trash Compactor")

# Part II
# --- main ---
# read data
file = open("input.data", "r")
# file = open("example.data", "r")
data = file.readlines()

lines = []
max_length = 0
for i in data:
  i = i.replace("\n", "")
  lines.append(list(i))
  max_length = max(max_length, len(i))

for i in lines:
  i.extend([" "] * (max_length - len(i)))

sum = 0
part = 0
operator = "+"
for idx in range(max_length):
  token = lines[-1][idx]
  # check if a new operator block starts
  if token == "+":
    operator = "+"
    sum += part
    part = 0
    print("\n")
  if token == "*":
    operator = "*"
    sum += part
    part = 1
    print("\n")
  # convert the charcters in a column to a number
  num_str = ""
  for line in lines[0:-1]:
    num_str += line[idx]
  num_str = num_str.strip()
  if num_str == "":
    continue
  # compute the result
  if operator == "+":
    part += int(num_str)
    print("+", num_str, end="")
  elif operator == "*":
    print("*", num_str, end="")
    part *= int(num_str)

if operator == "+":
  sum += part
elif operator == "*":
  sum += part

print("\n")
print("--- result for the worksheet:")
print(sum)