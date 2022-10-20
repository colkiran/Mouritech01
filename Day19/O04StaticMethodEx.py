
from datetime import datetime
import dateutils

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreateEmployee(cls, name, DOB):
        actdt = datetime.strptime(DOB, "%d/%m/%Y")
        ag = round(dateutils.years(datetime.now(), actdt), 0)
        return cls(name, ag)

    @staticmethod
    def isEligible(age):
        return "Eligible" if age > 20 else "Not Eligible"

emp1 = Employee.CreateEmployee("Mike", "23/09/1999")
emp1.get_details()
print(f"He is {Employee.isEligible(emp1.age)} for the Exams")