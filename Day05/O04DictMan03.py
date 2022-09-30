
print("items".center(40, "-"))
# combination of keys and values functions

emp = {
    'emp1':{'empname':'Jack', 'dob': '12/10/1980', 'dept': 'finance', 'desig': "MGR", 'location': 'Blr', 'sal': 85000},
    'emp2':{'empname':'Joe', 'dob': '1/5/1983', 'dept': 'Mkt', 'desig': "BDE", 'location': 'Che', 'sal': 45000},
    'emp3':{'empname':'Kevin', 'dob': '23/03/1981', 'dept': 'IT', 'desig': "Analyst", 'location': 'Pun', 'sal': 70000}
}

print("=" * 40 )
print()
print(f"emp :{emp}")

print("=" * 40 )
print()

print(f"emp1 :{emp['emp1']}")

print("=" * 40 )
print()

print(f"emp2 :{emp['emp2']}")

print("=" * 40 )
print()

print(f"emp3 :{emp['emp3']}")

print("=" * 40 )
print()

for ky, info in emp.items():
    print(ky)
    print("------")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))
emp1 = {'empname':'Jack', 'dob': '12/10/1980', 'dept': 'finance', 'desig': "MGR", 'location': 'Blr'}

emp2 = {'empname':'Joe', 'dob': '1/5/1983', 'dept': 'Mkt', 'desig': "BDE", 'sal': 45000}

print(f"emp1 :{emp1}")
print("-" * 40)

print(f"emp2 :{emp2}")
print("-" * 40)

emp1.update(emp2)

print(f"emp1 :{emp1}")

print("clear".center(40, "-"))
emp1 = {'empname':'Jack', 'dob': '12/10/1980', 'dept': 'finance', 'desig': "MGR", 'location': 'Blr'}

print(f"emp1 :{emp1}")

emp1.clear()

print(f"emp1 :{emp1}")


