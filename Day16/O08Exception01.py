
import sys

n = int(input("Enter a number :"))
d = int(input("Enter a number greater than 0 :"))

print(f"n :{n}")
print(f"d :{d}")

try:
    q = n / d
    print(f"q :{q}")
except:
    print("Exception Occured......")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])


