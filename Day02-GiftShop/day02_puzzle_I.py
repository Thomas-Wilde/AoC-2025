
print("Day 2 - Gift Shop")

# Using readlines()
file = open("input.data", "r")
# file = open("example.data", "r")
data = str(file.readlines()[0])

ranges = data.split(",")
sum = 0

for r in ranges:
    lo = (int) (r.split("-")[0])
    hi = (int) (r.split("-")[1])
    for i in range(lo,hi+1):
        number = str(i)
        length = (int) (len(number))
        left = number[0:(int)(length/2)]
        right = number[(int)(length/2):]
        if (left == right):
            print(i)
            sum += i

print("--- result ---")
print(sum)