

def bankFlow(fnc):  #HOF

    def helperFun(args):
        print("=" * 40)
        print("login into the server ......")
        fnc(args)               # callback
        print("logout of the server.......")
        print("_" * 40)

    return helperFun

@bankFlow                               # withdraw = bankFlow(withdraw)
def withdraw(amt):
    print(f"debited {amt}....")

@bankFlow
def deposit(amt):
    print(f"credited {amt}.....")

@bankFlow
def gift(amt):
    print(f"transfered {amt}......")

withdraw(10000)
deposit(50000)
gift(5000)
