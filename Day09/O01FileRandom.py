
"""
seek - used to move the file handle from one place to another
tell - used to know the position of the file handle
"""

FL = open("data.txt", "rb")

print(f"Postion :{FL.tell()}")

# pos = FL.seek(125, 0)
pos = FL.seek(85, 0)
print(f"position :{pos}")

pos = FL.seek(140, 1)
print(f"position :{pos}")

pos = FL.seek(-50, 1)
print(f"position :{pos}")

pos = FL.seek(0,2)
print(f"position :{pos}")

# pos = FL.seek(-10, 0)

FL.close()