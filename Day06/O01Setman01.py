
# add, update, pop, remove, discard
# union, intersection, difference, symmetric difference


s1 =  {1, 2, 3}
print(f's1 :{s1}')
print(type(s1))

print("-" * 40)
s2 = set(range(1, 11))
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = {1, 2, 3, 4, 5.2, 6.1, 7.9, 'eight', 'nine', 'ten', 'eleven', True, False,
      12 + 0j, 14 - 3j}
print(f"s3 :{s3}")
print(type(s3))


print("-" * 40)
s1 = {1, 2, 3}
s1.add(1)
s1.add(4)
s1.add(2)
s1.add(3)
s1.add(5)

print(f"s1 :{s1}")

s1.update([1, 2, 3])
s1.update([4, 5, 6])
s1.update([2, 3, 4])
s1.update([7, 8, 9])

print(f"s1 :{s1}")
print("-" * 40)

res = s1.pop()
print(f"res :{res}")
res = s1.pop()
print(f"res :{res}")
print(f"s1 :{s1}")

print("remove".center(40, "-"))
s1.remove(8)
s1.remove(5)
# s1.remove(1)
print(f"s1 :{s1}")

print("discard".center(40, "-"))
s1.discard(4)
s1.discard(7)
s1.discard(1)               # will not throw any error message if the num is not                                present

print(f"s1 :{s1}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A symmetric difference B :", A ^ B)
print("B symmetric difference A :", B.symmetric_difference(A))

# frozen set - immutable
f1 = frozenset([1, 2, 3, 4, 5])
print(f"f1 :{f1}")
print(type(f1))
