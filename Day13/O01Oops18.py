
class Animal:
    def eat(self):
        print("Animals eat.....")

class Bird(Animal):
    def fly(self):
        print("Birds fly......")

class Chicken(Bird):
    def disp(self):
        print("Chickens are breeded for consumption......")

    def fly(self):
        print("Chickens seldom fly......")


chick = Chicken()
chick.eat()
chick.fly()

cuckoo = Bird()
cuckoo.fly()