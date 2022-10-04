
fruits = [
    ('apple', 280),
    ('orange', 110),
    ('grapes', 135),
    ('gauva', 80),
    ('pineapple', 70),
    ('banana', 85),
    ('pears', 180),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")
print("-" * 40)

prices = ['fruit' for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit[0] for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit[1] for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit[1] * 0.9 for fruit in fruits]               # discount of 10%
print(prices)
print("-" * 40)

prices = [fruit[1] * 0.75 for fruit in fruits]              # discount of 25%
print(prices)
print("-" * 40)

fruits = [
    ('apple', 280),
    ('orange', 110),
    ('grapes', 135),
    ('gauva', 80),
    ('pineapple', 70),
    ('banana', 85),
    ('pears', 180),
    ('strawberry', 350)
]

expnsvFrts = [fruit for fruit in fruits if fruit[1] > 100]
print(expnsvFrts)
print("-" * 40)

expnsvFrts = [[fruit[0], fruit[1], fruit[1] * 0.75, fruit[1] * 0.9]
              for fruit in fruits if fruit[1] > 100]
print(expnsvFrts)

print("-" * 40)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"Sentence :{sentence}")

words = [word for word in sentence.split()]
print(words)
print("-" * 40)

words = [word for word in sentence.split() if word != 'the']
print(words)
print("-" * 40)

words = [[word, len(word)] for word in sentence.split() if word != 'the']
print(words)
print("-" * 40)

numbers = [36.5, 45.3, -23.4, 44.7, -12.3, -30.09, -56.6, 100]
# print all positive numbers
posNums = [number for number in numbers if number > 0]
print(posNums)

print("-" * 40)
# print the square of all numbers between 1 and 10
squares = [n ** 2 for n in range(1,11)]
print(f"squares :{squares}")

print("-" * 40)
boys = ['sachin', 'rohit', 'rahul', 'virat', 'yuvraj', 'dhoni']
girls = ['deepika', 'sonam', 'alia', 'shradha', 'katrina', 'kareena']

combine = [(boy, girl) for boy in boys for girl in girls]
print(combine)
print("-" * 40)

combine = list(zip(boys, girls))
print(combine)

