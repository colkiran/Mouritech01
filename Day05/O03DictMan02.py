
print('keys'.center(40, "-"))
player = {'name': 'sachin', 'runs': 135, 'oppn': "Newzealand", 'venue': 'Auckland', 'year': 1998}
print(f"player :{player}")

k = player.keys()
print(k)
print(type(k))

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))

player = {'name': 'sachin', 'runs': 135, 'oppn': "Newzealand", 'venue': 'Auckland', 'year': 1998}
print(f"player :{player}")

v = player.values()
print(v)
print(type(v))

for v in player.values():
    print(v, end=" ")
print()

print("fromkeys".center(40, "-"))
# covert a list into a dictionary, elements of list should become the keys
cities = ['blr', 'hyd', 'che', 'mum', 'del', 'kol', 'mys']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 23)
print(f"res2 :{res2}")

print("setdefault".center(40, "-"))
player = {'name': 'sachin', 'runs': 135, 'oppn': "Newzealand", 'venue': 'Auckland', 'year': 1998}
print(f"player :{player}")

player.setdefault("name", "Tendulkar")
player.setdefault('runs', 99)

player.setdefault('age', 34)
player.setdefault('gender', 'male')

print(f"player :{player}")

print("pop".center(40, "-"))

player = {'name': 'sachin', 'runs': 135, 'oppn': "Newzealand", 'venue': 'Auckland', 'year': 1998}
print(f"player :{player}")

res = player.pop('oppn')
print(f"res :{res}")

# res = player.pop('fname')
# print(f"res :{res}")

res1 = player.pop('venue')
print(f"res1 :{res1}")

print("popitem".center(40, "-"))

player = {'name': 'sachin', 'runs': 135, 'oppn': "Newzealand", 'venue': 'Auckland', 'year': 1998}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")
