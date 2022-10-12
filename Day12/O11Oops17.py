
class Animal:

    def __init__(self):
        print("Animal Ctor........")
        self.age = 1

    def eat(self):
        print('Animals eat.......')


class Birds(Animal):
    def __init__(self):         # overriding constructor
        super().__init__()
        self.size = '1 kilo'
        print("Bird Cotr........")

    def fly(self):
        print("Birds fly....")

cuckoo = Birds()
print(cuckoo.__dict__)
print(cuckoo.size)
# print(cuckoo.age)