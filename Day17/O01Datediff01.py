
from datetime import datetime

dt = datetime.now()
print(f"dt :{dt}")

print("-" * 40)
print("Day :", dt.strftime("%a"))
print("Day :", dt.strftime("%A"))

print("-" * 40)
print("Month :", dt.strftime("%b"))
print("Month :", dt.strftime("%B"))

print("-" * 40)
print("Date :", dt.strftime("%d"))
print("Date :", dt.strftime("%D"))
print("Date :", dt.strftime("%x"))

print("-" * 40)
print("Year :", dt.strftime("%y"))
print("Year :", dt.strftime("%Y"))

print("-" * 40)
print("Time :", dt.strftime("%T"))
print("Time :", dt.strftime("%X"))

print("-" * 40)
dt1 = dt.strftime("%d-%m-%y")
print(f"dt1 :{dt1}")

print("-" * 40)
dt2 = dt.strftime("%d-%m-%Y")
print(f"dt2 :{dt2}")