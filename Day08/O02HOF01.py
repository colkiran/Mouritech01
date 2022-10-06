
def callMe():
    print(f"Apples from ooty......")

def fun(fnc):
    print("Hello.....")
    fnc()
    print("Hi.......")
    print("-" * 40)

    def defineMe():
        print("Oranges from kanpur.....")

    return defineMe

def funCallback(fnc):
    print('Mera Bharath Mahan.....')
    fnc()
    print("India is great........")

funCallback(fun(callMe))

