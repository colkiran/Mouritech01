
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('runs', 120), ('oppn', ' SA'), ('venue', 'Dublin')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='rahul', runs=85, oppn='England', venue='lords')
print(F"d4 :{d4}")
print(type(d4))

# read
print("-" * 40)
d5 = {'name': 'Sachin', 'runs': 89, 'oppn': 'Aus', 'venue': 'perth'}

print(f"Name :{d5['name']}")
print(f"Oppn :{d5['oppn']}")
# print(f"age  :{d5['age']}")

# iterate through a dictionary
print("-" * 40)

for x in d5:
    print(x, "=>", d5[x])
print()

# modify
print("-" * 40)
print(f"d5: {d5}")
d5['runs'] = 98
d5['venue'] = 'gabba'
d5['age'] = 32
d5['year'] = 2003

print(f"d5: {d5}")

print("-" * 40)
# del
del d5['venue']
del d5['oppn']
print(f"d5: {d5}")

print("-" * 40)
print(d5.get('name', "Invalid key, Please enter a valid key..."))
print(d5.get('oppn', "Invalid key, Please enter a valid key..."))


print("-" * 40)
print(dir(d1))
