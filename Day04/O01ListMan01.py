
l1 = list()         # create a list
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 4, 'five', 'six', 'seven', 8.2, 9.5, 10.1, True, False, 12 + 1j, 13-4j]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l4 = [1, 2, 3, 4, 'five', 'six', 'seven', 8.2, 9.5, 10.1, True, False, 12 + 1j, 13-4j]

# read data
print(f"l4[0] :{l4[0]}")
print(f"l4[6] :{l4[6]}")
print(f"l4[9] :{l4[9]}")
print(f"l4[-1] :{l4[-1]}")

# iteration
print("-" * 40)
for i in l4:
    print(i, end=" ")
print()

# update or modify
print("-" * 40)
l4[4] = 4.5
l4[8] = 7.5                 # not inserting but replacing the value that is
                            # already existing

print(f"l4 :{l4}")

print("-" * 40)
# memory allocation is not contigious

print(f"l4[0] :{id(l4[0])}")
print(f"l4[1] :{id(l4[1])}")
print(f"l4[2] :{id(l4[2])}")
print(f"l4[3] :{id(l4[3])}")
print(f"l4[4] :{id(l4[4])}")

print("-" * 40)
values = list(range(10, 40, 10))
print(f"values :{values}")

# unpack the list and store it in different variables
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
values = list(range(10, 101, 10))
print(f"values :{values}")
a, b, *c = values           # *c can store more than one value
print(f"a :{a}, b :{b}, c :{c}")

a, *b, c = values           # b* can store more than one value
print(f"a :{a}, b :{b}, c :{c}")

*a, b, c = values           # *a can store more than one value
print(f"a :{a}, b :{b}, c :{c}")

print("-" * 40)
l1 = [1, 2, 3]
l2 = l1 * 2
print(f"l2 :{l2}")

print("-" * 40)
lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]

lst3 = lst1, lst2
print(lst3)
print(len(lst3))

print("-" * 40)
lst4 = [*lst1, *lst2]           # unpack
print(f"lst4 :{lst4}")
print(len(lst4))

print("-" * 40)
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = l1 + l2
print(f"l3 :{l3}")

