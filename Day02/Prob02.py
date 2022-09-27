
n = 0
for i in range(150, 49, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end = " ")
        n += 1

print(f"\nThere are {n} prime numbers between 150 and 50")