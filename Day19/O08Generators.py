
from sys import getsizeof

v1 = [x ** 2 for x in range(1, 11)]                 # compreshensions
print(v1)
print(type(v1))

print("-" * 40)
v2 = (x ** 2 for x in range(1, 11))
print(f"v2 :{v2}")
print(type(v2))
print(v2.__next__())
print(v2.__next__())
print(v2.__next__())

print("-" * 40)

res1 = sum([x ** 2 for x in range(1, 11)])
print(f"res1 :{res1}")

res2 = sum((x ** 2 for x in range(1, 11)))
print(f"res1 :{res1}")

print("-" * 40)

exp1 = [x ** 2 for x in range(1, 10000)]
exp2 = (x ** 2 for x in range(1, 10000))

print(f"Comprehension size of lst :{getsizeof(exp1)}")
print(f"Generator size of lst :{getsizeof(exp2)}")
