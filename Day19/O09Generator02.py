
def fun():
    n = 1
    print("Apples from Ooty")
    yield n
    n += 9
    print("Oranges from kanpur")
    yield n
    n += 10
    print("Grapes from Hubli")
    yield n

res = fun()
print(type(res))
# print(f"res :{res}")

print(res.__next__())

print("-" * 40)
print(res.__next__())

print("-" * 40)
print(res.__next__())

print("-" * 40)

def fun():
    for i in range(1, 11):
        yield(i)

gen = fun()
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

for x in fun():
    print(x, end=" ")
print()

