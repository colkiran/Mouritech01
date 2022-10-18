

try:
    n = int(input("Enter a number :"))
    d = int(input("Enter a number greater than 0 :"))

    print(f"n :{n}")
    print(f"d :{d}")


    q = n / d

except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
else:
    print(f"q :{q}")

finally:
    print("Division of number successfull")
