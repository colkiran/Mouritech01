
# Magic Methods
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

ply1 = Player("Micheal", 35)
# ply1.get_details()

print("-" * 40)
print(str(ply1))                # calls __str__()

print("-" * 40)
print(ply1)                     # implicitly call __str__

