
# emulate C syntax - prinf
format = "Welcome %s what a %s player"
print(format)
values = ("Sachin", "superb")                         # tuple
print(values)
print(format % values )

print("Welcome %s what a %s player" % ("Sachin", "superb"))

print("-" * 40)
format = "Welcome %s, your rating of %.3f, what a %s player"
print(format)
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.2, "class"))
print(format % ("Sachin", 4.2734345, "class"))
print(format % ("Sachin", 4.6899999, "class"))

# emulate unix shell syntax
print("-" * 40)
from string import Template
tmp = Template("Welcome $name, What a $adj player")
print(f"tmp :{tmp}")
res = tmp.substitute(name= "Sachin", adj ="class")
print(f"res :{res}")

# format from strings of python
print("-" * 40)
# *args
print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcome {1}, what a {2} player for {0}".format("India", "Sachin", "class"))
# **kwargs
print("Welcome {name}, what a {adj} player for {ctr}".format(name="Sachin", adj="class", ctr="India"))

print("-" * 40)
print("Welcome {name}, your rating of {rating}, what a {adj} player for {ctr}".format(
    name= "Sachin", rating=4, adj="class", ctr="India"))

print("Welcome {name}, your rating of {rating:.3f}, what a {adj} player for {ctr}".format(
    name= "Sachin", rating=4.8, adj="class", ctr="India"))

# interpolation
print("-" * 40)
print("-" * 40)
from math import pi, e
print(f"PI = {pi} and Eulers Constant = {e}")

print("PI = {} and Eulers Constant = {}".format(pi, e))
print("PI = {} and Eulers Constant = {} and magic number = {magic}".format(pi, e, magic=40585))
print("PI = {0} and Eulers Constant = {1} and magic number = {magic}".format(pi, e, magic=40585))

print("-" * 40)
fullname = ['Rahul', 'Dravid']
print("Mr. {name}".format(name = fullname))
print("Mr. {name[0]} {name[1]}".format(name=fullname))

print("-" * 40)
import math
print(__name__)
print(math.__name__)

print("The {mod.__name__} module gives the value of pi={mod.pi} and Euler's e = {mod.e}".format(mod=math))

# conversions
print("conversions".center(40,"-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 40)
print("the number {num} {num} {num}".format(num=36))
print("the number {num} {num:f} {num:b}".format(num=36))
print("the number {num:10} {num:f} {num:b}".format(num=36))
print("the number {num:5} {num:f} {num:b}".format(num=36))
print("the number {num:5} {num:f} {num:b}".format(num=36345778679))

print("Alignment".center(40, "-"))
print('{num:15} Tendulkar'.format(num="Sachin"))
print('{num:15} Tendulkar'.format(num=150))
print('{}'.format("Sachin Tendulkar"))
print('{:.6}'.format("Sachin Tendulkar"))
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))

print("-" * 40)
print("{label:40}".format(label="Python"))
print("{label:*<40}".format(label="Python"))                # left aligned
print("{label:*^40}".format(label="Python"))                # center aligned
print("{label:*>40}".format(label="Python"))                # right aligned

print("-" * 40)
print("{label:<40}".format(label="Python"))                # left aligned
print("{label:^40}".format(label="Python"))                # center aligned
print("{label:>40}".format(label="Python"))                # right aligned

print("-" * 40)
print("{label:<40}".format(label="10124"))                # left aligned
print("{label:^40}".format(label="10124"))                # center aligned
print("{label:>40}".format(label="10124"))                # right aligned



