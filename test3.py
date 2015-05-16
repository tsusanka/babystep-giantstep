
from random import randint
from bisect import bisect_left

def value_exists(needle, haystack):
    # finds if needle exists in haystack of tuples and returns it if so
    i = bisect_left(haystack, needle)
    if i != len(haystack) and haystack[i] == needle:
        return i
    else:
        return -1

n = 200000
size = 10

# fill array A with random numbers
arrayA = [1]
for i in range(1, n):
    arrayA.append(randint(0, size))

arrayA = enumerate(arrayA)
# sort them by values keeping its indexes
arrayA = sorted(arrayA, key=lambda x: x[1])

# search
for i in range(1, n):
    check = value_exists(randint(0, size), arrayA)
    if check != -1:
        break

print(check)
print(arrayA[check])
