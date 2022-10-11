
class Player:

    team = "India"

    def __init__(self, name, age):
        print("Player Ctor.....")
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    # @classmethod
    # def ChangeAttr(cls, tm):
    #    cls.team = tm

    @classmethod
    def CreatePlayer(cls, firstname, lastname, age):
        print("factory....")
        return cls(f"Mr.{firstname} {lastname}", age)                # calls the constructor

ply1 = Player("Sachin", 30)
ply1.get_details()
print("-" * 40)

ply2 = Player.CreatePlayer("Rahul", "Dravid", 28)
ply2.get_details()


"""
ply1 = Player("Rahul", 30)
ply2 = Player("Yuvraj", 28)

ply1.get_details()

print("-" * 40)
ply2.get_details()

print("-" * 40)
print(f"Team :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply3 :{ply2.team}")

print("-" * 40)
Player.ChangeAttr("Team Sahara")
print(f"Team :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply3 :{ply2.team}")
"""
