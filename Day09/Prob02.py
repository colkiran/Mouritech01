
FL = open("EMP.csv", "r")

gender = {}
dept = []
desig = []
sal = 0

for line in FL.readlines():
    g = line.split(",")[2]
    ds = line.split(",")[3]
    dp = line.split(",")[4]

    if g not in gender:
        gender[g] = 1
    else:
        gender[g] += 1

    if ds not in desig:
        desig.append(ds)

    if dp not in dept:
        dept.append(dp)

    sal += int(line.split(",")[5])

FL.close()

for k in gender.keys():
    if k == "m":
        print(f"Male   :{gender[k]}")
    else:
        print(f"Female :{gender[k]}")

print(f"Designation :{desig}")
print(f"Department  :{dept}")
print(f"Salary      :{sal}")
