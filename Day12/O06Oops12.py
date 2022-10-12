
class Employee:

    def __init__(self, name):
        self.__name = name          # private variable
        self.tech = ['C', 'C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'NodeJS']

    def __str__(self):
        return self.__name + " - " + ",".join([t for t in self.tech])

e1 = Employee("Stephen")
print(e1)

print("-" * 40)
# print(e1.__name)
# e1.__name = "Richards"
print(e1.__dict__)

print("-" * 40)
print(e1._Employee__name)

print("-" * 40)
e1._Employee__name = "Richards"
print(e1.__dict__)