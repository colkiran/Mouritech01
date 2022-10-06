
def bankFlow(fnc):  #HOF
    print("=" * 40)
    print("login into the server ......")
    fnc()               # callback
    print("logout of the server.......")
    print("_" * 40)

def withdraw():
    print("debited....")

def deposit():
    print("credited.....")

def gift():
    print("transfered......")

bankFlow(withdraw)
bankFlow(deposit)
bankFlow(gift)
