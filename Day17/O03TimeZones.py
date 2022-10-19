"""
UTC - it helps to get the standard UTC time zone
(universal time coordinates)
timezone() = to get the time zone of a particular location
now()   - gets the current date and time stamp
astimezone() - to convert the time of particular timezone into another timezone
"""

import time
from datetime import datetime
import pytz

curtime = time.localtime()
# print(curtime)
curclock = time.strftime("%H:%M:%S", curtime)
print(curclock)

print("=" * 40)

utc = pytz.utc
print(f"utc :{utc}")

IST = pytz.timezone('Asia/Kolkata')
print(f"IST :{IST}")

print("-" * 40)
print("utc default format :", datetime.now(utc))

print("IST default format :", datetime.now(IST))

print("-" * 40)

IST = pytz.timezone('Asia/Kolkata')
NYT = pytz.timezone('America/New_York')
UKT = pytz.timezone('Europe/London')
AST = pytz.timezone('Australia/Melbourne')

print("IST format :", datetime.now(IST))
print("NYT format :", datetime.now(NYT))
print("UKT format :", datetime.now(UKT))
print("AST format :", datetime.now(AST))

