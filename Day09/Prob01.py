
ch = "y"
st = ""
while ch == 'y':
    s = input("Enter the contents of the file :")
    st += s + "\n"
    ch = input("Do you want to continue y / n:")

FW = open("myfile.txt", "w")
FW.write(st)
FW.close()
