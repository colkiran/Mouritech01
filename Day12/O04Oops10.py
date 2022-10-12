
class Arun:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, x):
        return self.salary + x.salary

    def __sub__(self, x):
        return self.salary - x.salary

    def __mul__(self, x):
       return self.salary * x.salary

    def __truediv__(self, x):
        return self.salary / x.salary

    def __floordiv__(self, x):
        return  self.salary // x.salary

a1 = Arun("John", 45000)
a2 = Arun("George", 20000)

print(f"Addition :{a1 + a2}")

print(f"Subtraction :{a1 - a2}")

print(f"Multiplication :{a1 * a2}")

print(f"Division :{a1 / a2}")

print(f"Floor Div :{a1 // a2}")

