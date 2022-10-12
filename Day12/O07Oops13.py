
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        if val < 0:
            raise ValueError("Price cannot be less than zero(0)")
        else:
            self.__price = val


import sys
try:
    pepsi = Product(30)
    print("Price is :", pepsi.get_price())
    pepsi.set_price(50)
    print("Price is :", pepsi.get_price())

    # pepsi.set_price(-50)
    # print("Price is :", pepsi.get_price())
except:
    print("Exception Raised....")
    print(sys.exc_info()[0], "Occured")
    print(sys.exc_info()[1])
