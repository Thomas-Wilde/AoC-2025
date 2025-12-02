
print("Day 2 - Gift Shop")

def isValid(number:int)->bool:
    number = int(number)
    modder = 10
    # print(number)
    while number % modder != number:
        num_copy = number
        parts = []
        while num_copy > 0:
            part = num_copy%modder
            if (part*10 < modder):
                parts.append(-1)
            parts.append(part)
            num_copy = num_copy//modder

        passed = bool(True)
        check = parts[0]
        for i in parts:
            if check != i:
                passed = False
                break
        if passed:
            print(parts)
            return True;
        modder = modder * 10
    return False


# Using readlines()
file = open("input.data", "r")
# file = open("example.data", "r")
data = str(file.readlines()[0])

ranges = data.split(",")
sum = 0

sum = 0
for r in ranges:
    lo = (int) (r.split("-")[0])
    hi = (int) (r.split("-")[1])
    for i in range(lo,hi+1):
        number = str(i)
        if isValid(number):
            print(number)
            sum = sum + int(number)
        # length = (int) (len(number))
        # left = number[0:(int)(length/2)]
        # right = number[(int)(length/2):]
        # if (left == right):
        #     print(i)
        #     sum += i

print("--- result ---")
print(sum)