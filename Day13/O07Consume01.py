
import mymodule as m
from mymodule import Employee

print(m.gname)
print(m.runs)
print(m.sports)

emp1 = Employee("Bob", 45000)
emp1.get_details()

emp2 = Employee("Joe", 65000)
emp2.get_details()
