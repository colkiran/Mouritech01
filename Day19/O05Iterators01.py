
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")

iterObj = l.__iter__()              # iter(l)
# print(dir(iterObj))
# __iter__, __next__ these two methods are the protocol of iterable object

e1 = iterObj.__next__()
print(f"Element01 - {e1}")

print("-" * 40)
e2 = iterObj.__next__()
print(f"Element01 - {e2}")

print("-" * 40)
e3 = iterObj.__next__()
print(f"Element01 - {e3}")

print("-" * 40)
e4 = iterObj.__next__()
print(f"Element01 - {e4}")

print("-" * 40)
e5 = iterObj.__next__()
print(f"Element01 - {e5}")

# print("-" * 40)
# e6 = iterObj.__next__()
# print(f"Element01 - {e6}")

print("-" * 40)
for x in l:
    print(x, end=" ")
print("")
