
class Singleton:

    __shared_instance = "Singleton Example"

    @staticmethod
    def getInstance():
        if Singleton.__shared_instance == "Singleton Example":
            Singleton()
        return Singleton.__shared_instance

    def __init__(self):
        if Singleton.__shared_instance != 'Singleton Example':
            raise Exception("This is a singleton class..")
        else:
            Singleton.__shared_instance = self


if __name__ == '__main__':

    obj1 = Singleton()
    print(obj1)

    obj2 = Singleton.getInstance()
    print(obj2)
