
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.salary}"

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee("Kenith", 40000)
print(emp1)

print("-" * 40)
emp2 = Employee("Kevin", 40000)
print(emp2)

print("-" * 40)
if emp1 != emp2:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)
if emp1 < emp2:
    print("{}'s salary of {} is Less Than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is Greater Than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

