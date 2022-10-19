
from datetime import datetime
import dateutils

dt3 = "Wednesday, September 30, 2020"
print(f"dt3 :{dt3}")
print(type(dt3))

print("-" * 40)
dt4 = "Sunday, October 31, 2021"
print(f"dt4 :{dt4}")
print(type(dt4))

print("-" * 40)
# difference between dt3 and dt4
actdt1 = datetime.strptime(dt3, "%A, %B %d, %Y")
print(f"Actdt1 :{actdt1}")
print(type(actdt1))

print("-" * 40)
actdt2 = datetime.strptime(dt4, "%A, %B %d, %Y")
print(f"actdt2 :{actdt2}")
print(type(actdt2))

print("-" * 40)
print(actdt2 - actdt1)

print("-" * 40)
print('Difference in days :',dateutils.days(actdt2, actdt1))

print("-" * 40)
print("Difference in Weeks :", dateutils.weeks(actdt2, actdt1))

print("-" * 40)
print("Difference in months :", dateutils.months(actdt2, actdt1))

print("-" * 40)
print("Difference in years :", dateutils.years(actdt2, actdt1))
