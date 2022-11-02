
class Singleton:

    __instance = None
    __inited = False

    def __new__(cls) -> 'Singleton':
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if type(self).__inited:
            return
        type(self).__inited =True
        self.value = 10


Sobj1 = Singleton()
print(Sobj1)

Sobj2 = Singleton()
print(Sobj2)
