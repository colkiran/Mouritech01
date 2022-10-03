
def addMe(x, y):
    return x + y

# print(addMe(10, 20))

a = addMe
print(a(10, 20))

print("-" * 40)

b = lambda x, y: x + y
print( b(100, 200) )

#lambda's are best used with other functions like - map, reduce and filter

print("-" * 40)
# map -> expression is implemented on each and every value
l = list(range(1, 11))
print(f"l :{l}")

squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

# conversions => temp(cel - faren), weights(kgs - lbs), currency (rs - dollars)
# sort the list
months = ['dec', 'aug', 'apr', 'nov', 'feb', 'jul', 'oct', 'jan', 'mar', 'sep', 'may', 'jun' ]
print(f"months :{months}")

from calendar import month_name
asc_res = sorted(months, key=list(map(lambda mth :mth[0:3].lower(), list(month_name))).index)

print(f"Ascending order :{asc_res}")

print("-" * 40)
# filters - result of the expression should return a true or false

l = list(range(1, 25))
print(f"l :{l}")

st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

res = list(filter(lambda x: x != 'the', st.split()))
print(f"res :{res}")

print("-" * 40)
# reduce - functools
from functools import reduce
# reduce - reduce the size of the list into a single value

l = [8, 3, 4, 7, 9, 5, 6, 10]
print(f"l :{l}")

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

print("-" * 40)
res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")
