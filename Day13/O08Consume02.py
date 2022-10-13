
import mypackage.mymodule as m
from  mypackage.mymodule import Employee

m.gname = "Rahul Dravid"
print(m.gname)
print(m.runs)
print(m.sports)

emp1 = Employee("Peter", 45000)
emp1.get_details()

emp2 = Employee("Richard", 65000)
emp2.get_details()

m.greet("Mahendra Singh Dhoni")
