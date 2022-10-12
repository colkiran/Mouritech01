
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = 1

    def eat(self):
        print("Animals eat.....")

# inheritance

class Bird(Animal):

    def fly(self):
        print("Birds fly....")


class Fish(Animal):

    def swim(self):
        print("Fishes swim.......")


print('-' * 40)
cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()

print('-' * 40)
dolphin = Fish()
dolphin.swim()
dolphin.eat()

print('-' * 40)
print(cuckoo.__dict__)
print(dolphin.__dict__)

print('-' * 40)
print(f"isinstance(cuckoo, Bird)", isinstance(cuckoo, Bird))
print(f"isinstance(cuckoo, Animal)", isinstance(cuckoo, Animal))
print(f"isinstance(dolphin, Fish)", isinstance(dolphin, Fish))
print(f"isinstance(dolphin, Animal)", isinstance(dolphin, Animal))

print('-' * 40)
print(f"isinstance(dolphin, Bird)", isinstance(dolphin, Bird))
print(f"isinstance(cuckoo, Fish)", isinstance(cuckoo, Fish))

