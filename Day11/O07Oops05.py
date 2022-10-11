"""
Accessing means changing the value, if we are not able to change the value then we cannot access that variable (printing is allowed)

"""
class Player:

    team = "India"              # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 34)
ply1.get_details()
print("-" * 40)

ply2 = Player("Sourav", 33)
ply2.get_details()
print("-" * 40)

print(f"Player :{Player.team}")
print(f"Ply1 :{ply1.team}")
print(f'Ply2 :{ply2.team}')

print("-" * 40)
Player.team = "MI"
print(f"Player :{Player.team}")
print(f"Ply1 :{ply1.team}")
print(f'Ply2 :{ply2.team}')

print("-" * 40)
ply2.team = "KKR"
print(f'Ply2 :{ply2.team}')

print(f"Player :{Player.team}")
print(f"Ply1 :{ply1.team}")

print("-" * 40)
print(f"ply2 :{ply2.__dict__}")

print("-" * 40)
print(f"Player :{Player.__dict__}")
