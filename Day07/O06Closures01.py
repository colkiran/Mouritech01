
# closure
def outerFun(gname):
    gst = f"Mr.{gname}"

    def innerFun():
        print("hello world")
        print(f"Greetings {gname}")
        print(f"Greetings {gst}")

    #outerfunction
    innerFun()
    print(f"After innerfun call.....")

outerFun("Sachin")