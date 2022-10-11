"""
self in methods
---------------
will take the name of the object that made a call to the method

"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 30)
ply2.get_details()

print("-" * 40)
print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)

print("-" * 40)
ply2.runs = 75
print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)
