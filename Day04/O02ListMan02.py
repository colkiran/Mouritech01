
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 40)
for letter in letters:
    print(letter, end=' ')
print("")

print("-" * 40)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter[0], letter[1])
print()

print("-" * 40)
for index, letter in enumerate(letters):
    print(index, letter)
print()

print("-" * 40)
mylist = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 40)
for lst in mylist:
    print(lst)

print("-" * 40)
for ind, lst in enumerate(mylist):
    print(f"{ind}\t{lst}")

print("-" * 40)
for ind, lst in enumerate(mylist):
    print(f"List({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")


print("-" * 40)
for lst in mylist:
    for num in lst:
        print(num, end=" ")
    print()
print()

print("-" * 40)
print(dir(mylist))

