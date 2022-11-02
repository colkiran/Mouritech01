
class Shape(object):
    pass

def factory(type):

    class Circle(Shape):
        def draw(self): print("Circle draw......")

        def erase(self): print("Erase circle......")

    class Square(Shape):
        def draw(self): print("Square draw.......")

        def erase(self): print("Erase square......")

    class Triangle(Shape):
        def draw(self): print("Triangle draw.....")

        def erase(self): print("Erase triangle.....")

    if type == 10:
        return Circle()
    if type == 20:
        return Square()
    else:
        return Triangle()

shape = factory(30)
if shape != None:
    shape.draw()
    shape.erase()
# else:
#     print("Wrong shape key....")