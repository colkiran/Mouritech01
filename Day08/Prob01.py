

def outside(fnc):
    def inside(*args):
        fnc(*args)
        print("-" * 40)
    return inside

def fun():
    print("Function fun called....")

def fun1(x):
    print(f"Function fun called....{x}")

def fun2(x, y):
    print(f"Function fun called....{x}, {y}")

def fun3(x, y, z):
    print(f"Function fun called....{x}, {y}, {z}")

def fun4(x, y, z, n):
    print(f"Function fun called....{x}, {y}, {z}, {n}")

f = outside(fun)
f1 = outside(fun1)
f2 = outside(fun2)
f3 = outside(fun3)
f4 = outside(fun4)

f()
f1(10)
f2(100, 200)
f3(11, 22, 33)
f4(10, 20, 30, 40 )

