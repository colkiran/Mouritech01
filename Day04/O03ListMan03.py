
print("{:-^40}".format("append"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.append(11)
l1.append(12)
l1.append(13)

print(f"l1 :{l1}")

l1.append([14, 15, 16, 17, 18])
print(f"l1 :{l1}")
print(l1[13][1:4])
print(l1[-1][1:4])

print("extend".center(40, "-"))
l2 = list(range(1, 11, 2))
print(f"l2 :{l2}")

l2.extend([11, 13, 15, 17, 19])
print(f"l2 :{l2}")

print("insert".center(40,"-"))
l1 = [1, 2, 3, 4, 5]
print(f'l1 :{l1}')

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")
l1.insert(15, 6)
print(f"l1 :{l1}")
print(len(l1))

print("pop".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop(6)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(40, "-"))
l1 = [1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 3, 1, 1, 2, 1, 2, 3 ]
print(f"l1 :{l1}")
print(l1.remove(3))

print(f"l1 :{l1}")

while l1.count(1):
    l1.remove(1)

# while True:
#     try:
#         l1.remove(1)
#     except ValueError:
#         break

print(f"l1 :{l1}")

print("clear".center(40,"-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

