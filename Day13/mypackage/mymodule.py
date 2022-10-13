
gname = "Sachin Tendulkar"

sports = ['cricket', 'tennis', 'hockey', 'football', 'swimming']

runs = {'test': 23000, 'odis': 19500, 't20': 1500}

def greet(gst):
    print(f"Greetings Mr.{gst}, Welcome to the event......")

def sum(x, y):
    return x + y

class Employee:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def get_details(self):
        print(f"Name is {self.name}\nSalary is {self.salary}")
        print(f"There are totally {Employee.empCount} employees")
        print("-" * 40)

