
FL = open("data.txt", "r")
print(type(FL))
print("-" * 40)
print("\n")

# st = FL.read(1500)
# print(st)

# st = FL.readline()
# print(st)
#
# print("_" * 40)
# st = FL.readline()
# print(st)

# for line in FL.readlines():
#     print(line)

st = FL.readlines(860)
print(st)


FL.close()