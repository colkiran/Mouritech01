
#HOF
def outerFun(greet):

    def innerFun(gname):
        print(greet, gname)

    return innerFun


outerFun("Welcome")("Sachin")           # directly call the innerfun
print("-" * 40)

# curry
engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakam")

# simple curry
engGrt("Rahul")
hndGrt("Jadeja")
tmlGrt("Natraj")
