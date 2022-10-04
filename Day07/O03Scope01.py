
glbX = 100

def fun(a):                     # a is a local variable
    global glbX
    glbX = 500
    print(f"inside :{glbX}")
    b = "hello world"           # b is a local variable
    print(f"b :{b}")
    print(f"a :{a}")

print(f"before :{glbX}")

fun(20)

print(f"after :{glbX}")