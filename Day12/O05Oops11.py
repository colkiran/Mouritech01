
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'NodeJS']

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.salary}"

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val

e1 = Employee("David", 18500)
print(e1)

print("-" * 40)
print([e for e in e1])              # LIST COMPREHENSION

print("-" * 40)
e1.append("Python")

print("-" * 40)
print([e for e in e1])

print("-" * 40)
x = e1[5]
print(x)

print("-" * 40)
e1[3] = "JSP"
print([e for e in e1])