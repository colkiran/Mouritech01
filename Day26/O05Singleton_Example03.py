
class Singleton:

    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            Singleton.__instance
        else:
            Singleton.__instance = self



s3 = Singleton()
print(s3)
s3.val = 10

s2 = Singleton.get_instance()
print(s2)
print(s2.val)

s1 = Singleton()
print(s1)
# print(s1.val)