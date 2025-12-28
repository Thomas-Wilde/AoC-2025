print("Day 6 - Trash Compactor")

# Part I
# --- main ---
# read data
file = open("input.data", "r")
# file = open("example.data", "r")
data = file.readlines()

lines = []
for i in data:
     lines.append(i.strip())

tokens = []
for line in lines:
  tokens_line = line.split()
  tokens.append(tokens_line)
tokens.reverse()

for token in tokens:
  print(token)

numbers_per_line = len(tokens[0])
sum = 0
for i in range(numbers_per_line):
  operator = tokens[0][i]
  # initialize result
  result = 0
  if operator == "+":
    result = 0
  elif operator == "*":
    result = 1
  # calculate result
  for token_line in tokens[1::]:
    if operator == "+":
      result += int(token_line[i])
    elif operator == "*":
      result *= int(token_line[i])
  sum += result

print("--- result for the worksheet:")
print(sum)

# Part II