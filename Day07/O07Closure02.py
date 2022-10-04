
# closure
def outerFun(gname):                # HOF - Higher order function
    gst = f"Mr.{gname}"

    def innerFun():
        print("hello world")
        print(f"Greetings {gname}")
        print(f"Greetings {gst}")

    return innerFun

outerFun("Sachin")
print("-" * 40)

infun = outerFun("Sachin")
print("After few lines of code.....")
infun()
print("-" * 40)

print(__name__)     # __main__
print(outerFun.__name__)
print(outerFun("Sachin").__name__)