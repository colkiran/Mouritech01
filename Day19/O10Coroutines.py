
def get_name(surname):
    print(f"Surname is {surname}")

    while True:
        name = yield                # accepting value from the user
        print(f"Name received....{name}")
        print("-" * 40)
        if surname in name:
            print(f"surname {surname} found in {name}......")

coObj = get_name("birla")
print(coObj)
coObj.__next__()
coObj.send("ratan tata")
coObj.send("anil ambani")
coObj.send("aditya birla")
