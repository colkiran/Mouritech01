
def outerFun(gname):
    guest = f"Mr.{gname}"

    def innerFun():
        nonlocal gname        # only local variables can be converted to non local
        gname = "Mohammed Ali"                   # local variable
        print(f"hello {gname}")

    innerFun()
    print(f"After :{gname}")

outerFun("Mike Tyson")
