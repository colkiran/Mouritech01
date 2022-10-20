
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")

itrObj = iter(l)

while(True):
    try:
        elem = next(itrObj)
        print(f"elem :{elem}")
    except StopIteration:
        break

