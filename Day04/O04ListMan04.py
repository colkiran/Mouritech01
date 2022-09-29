
print("count".center(40, "-"))
l1 = [1, 2, 3, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3]
print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"5 :{l1.count(5)}")

print("index".center(40, "-"))
l1 = [1, 2, 3, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3]
print(f"l1 :{l1}")

idx = l1.index(3)
print(f"index :{idx}")

idx = l1.index(3, l1.index(3) + 1)
print(f"index :{idx}")

idx = l1.index(3, l1.index(3, l1.index(3) + 1) + 1)
print(f"index :{idx}")

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")
l2 = l1                 # shallow copy   -> shares the data with the address
print(f"l2 before :{l2}")

l2.extend([6, 7, 8, 9])
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 40)
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")
l4 = l3.copy()          # deep copy -> share only the data
print(f"l4 before :{l4}")

l4.insert(1, 65)
l4.insert(3, 75)
l4.insert(5, 85)

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 40)
l5 = [10, 20, 30, [5, 10, 15, 20, 25], 40, 50]
print(f"l5 before :{l5}")
l6 = l5.copy()          # deep copy
print(f"l6 before :{l6}")

# print(l6[3])
l6[3].extend([30, 35, 40, 45])
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 40)
l7 = [1, 2, 3, 4, [3, 6, 9, 12, 15], 5]
print(f"l7 before :{l7}")
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[4].extend([18, 21, 24])
print(f"l8 after :{l8}")
print(f"l8 after :{l7}")
