import time


def outerFun(fnc):

    def helperFun(x, y):
        if y > x:
            x, y = y, x
        print(f"x :{x}\ty :{y}")
        print(fnc(x, y))
        print("-" * 40)

    return helperFun

@outerFun
def diff(x, y):
    return x - y

diff(20, 8)
diff(8, 20)

print("-" * 40)

def outerFun(fnc):

    def helperFun(val):
        st = time.perf_counter()
        fnc(val)
        et = time.perf_counter()
        print(f"The total time taken by the function {fnc.__name__} to execute is {et - st}")

    return helperFun


@outerFun
def fun(n):
    l = []
    for i in range(n):
        for j in range(1, i+1):
            l.append(j ** 2)

fun(6000)
