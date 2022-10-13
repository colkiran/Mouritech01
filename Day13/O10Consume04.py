
import gurgaon.mymodule as m
from gurgaon.mymodule import Employee

import sys

for pth in sys.path:
    print(pth)

print("hello world")

print("=*" * 40)
m.greet('Verendra Sehwag')

emp1 = Employee("John", 60000)
emp1.get_details()

emp2 = Employee("Kennedy", 60000)
emp2.get_details()

