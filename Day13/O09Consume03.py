
import sys

sys.path.append("C:\\Delhi")

for pth in sys.path:        # sys.path is a list
    print(pth)

import gurgaon.mymodule as m
from gurgaon.mymodule import Employee

print("=*" * 40)
m.greet('Sourav Ganguly')

emp1 = Employee("Adam", 60000)
emp1.get_details()

emp2 = Employee("Nixon", 60000)
emp2.get_details()

