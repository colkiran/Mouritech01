
print("sort".center(40, "-"))
l = [8, 5, 2, 1, 10, 3, 9, 6, 4, 5]
print(f"l :{l}")

# sort the numbers
res1 = sorted(l)
print(f"Ascending order  :{res1}")

l.sort(reverse=True)
print(f"Descending order :{l}")

print("-" * 40)
l = [8,'zebra', 'apple', 5, 'yellow', 'blue', 2, 'white', 'green', 1, 'violet', 'maroon', 10, 'pink', 'magenta', 3, 'xmas', 'cat', 9, 'dog', 'frog', 6, 'hen', 'nose', 4, 5, 185, 1024, 29, 265, 2341, 370, 3450, 39]
print(f"l :{l}")

print("-" * 40)
res = sorted(l, key=ascii)
print(f"res :{res}")

print("-" * 40)
cities = ['kanyakumari', 'bangalore', 'delhi', 'ooty', 'hyderabad', 'chennai', 'thiruvananthapuram', 'mumbai', 'pune', 'vishakapatnam', 'kolkotta']
print(f"cities :{cities}")

print("-" * 40)
print()
res1 = sorted(cities, key=len)
print(f"Ascending :{res1}")

print("-" * 40)
print()
res2 = sorted(cities, key=len, reverse=True)
print(f"Descending :{res2}")

print("-" * 40)
print()

# sort it according to the calendar, write a function and pass the function as key

months = ['dec', 'aug', 'apr', 'nov', 'feb', 'jul', 'oct', 'jan', 'mar', 'sep', 'may', 'jun' ]
print(f"months :{months}")

print("-" * 40)
print()

from calendar import month_name
print(list(month_name))

l = []
for mth in list(month_name):
    l.append(mth[0:3].lower())

print("-" * 40)
print()

print(l)

print("-" * 40)
print()

def sort_month(mon):
    if mon in l:
        return l.index(mon)

res_asc = sorted(months, key=sort_month)
print(f"Asc :{res_asc}")

print("-" * 40)
print()

res_des = sorted(months, key=sort_month, reverse=True)
print(f"Desc :{res_des}")

print("reverse".center(40, "-"))
l = [8, 5, 2, 1, 10, 3, 9, 6, 4, 5]
print(f"l :{l}")

res = list(reversed(l))
print(f"res :{res}")

