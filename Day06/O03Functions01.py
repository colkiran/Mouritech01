
def greet():
    print("Greetings Mr. Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")

# city is a default arg and gname is a non default argument
def greetGstCty(gname,  city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event")

greet()
greetGst("Rahul")
greetGst("Sachin")
greetGstCty('Sachin')
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

# /Return value

def addMe(x, y):
    return x + y

a = 10
b = 20

print("-" * 40)
print(f"The sum if {a} and {b} is :{addMe(a, b)}")

print("-" * 40)
print("The sum of %d and %d is :%d" % (a, b, addMe(a, b)))

print("-" * 40)
# named tuple
def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod =  x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmeticCalc(20, 8)
print(f"res :{res}")

print("-" * 40)

def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x - 1)

n = 5
print(f'The factorial of {n} is :{fact(n)}')

print("-" * 40)
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

iter = int(input("Enter the number of iterations :"))

print("Fibanocci series....")
for i in range(iter):
    print(fibo(i), end=" ")
print()

print("-" * 40)
# taking args into a function
# args to a function

def admisn(name, dob, gender, conno, qlf, addr, city):
    print(f"Name          :{name}")
    print(f"DOB           :{dob}")
    print(f"Gender        :{gender}")
    print(f"Contact No.   :{conno}")
    print(f"Qualification :{qlf}")
    print(f'Address       :{addr}')
    print(f"City          :{city}")


# *args => list
admisn("Jack", "10/12/1980", "Male", "349234023", 'BTech', "Indiranagar, 12th main", "Bangalore")

print("-" * 40)
print("-" * 40)
# **kwargs -> dictionary
admisn(addr = "Indiranagar, 12th main", gender="Male", dob="10/12/1980", qlf="Btech", city="Bangalore", conno="392349234" , name="Jill")

# admisn(*args, **kwargs)

# Variable length args
print("-" * 40)
def multiAll(*numbers):             # we can accept more than one arg like list
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(multiAll(1, 2, 3, 4, 5))

print("-" * 40)
def extracDetails(**details):
    print(details)
    for k in details:
        print(k, "=>", details[k])

extracDetails(name="sachin", runs=135, oppn="WI", venue="Sabina Park")

print("-" * 40)
# docstrings

def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)              # double underscore doc => dunder_doc
print("-" * 40)
print("-" * 40)

def fun1(x, y):
    """
    fun1(x, y)
    ----------

    this fun will take two args and
    if both the arguments are integer then the result is the sum of the integers
    if both the arguments are strings then the result will be a concatenation
    """

    return x + y

print(fun1(10,30))
print(fun1("hello", "world"))

print("-" * 40)
help(fun1)
