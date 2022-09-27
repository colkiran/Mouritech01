
for i in range(5):
    print("hello ", i)

print("-" * 40)

for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(3, 25, 3):
    print(i, end=" ")
print()

print("-" * 40)
for i in range(1, 25):
    if i % 3 == 0:
        print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 25):
    # if i > 20:
    #     break                               # terminate the iteration
    if i % 2 == 1:
        continue                            # skip the iteration
    print(i, end = " ")
else:
    print("\nCompleted the iteration.....")

