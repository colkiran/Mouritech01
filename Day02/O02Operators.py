
"""
1. arithmetic
2. comparison or relational
3. logical
4. bitwise
5. Ternary
"""

print("Arithmetic Operators".center(40,"-"))
print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")           # floor division
print(f"10 % 3 = {10 % 3}")
print(f"10 ** 3 = {10 ** 3}")

print("Augmentor Operator".center(40, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")
x += 5
print(f"x :{x}")
x /= 3
print(f"x :{x}")

print("Comparison Operator".center(40, "-"))
# ==, >=, <=, !=
a = 10
b = 20
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)

print("logical operators".center(40, "-"))
# and, or, not
print(1 == 1 and 2 == 2)
print(1 == 2 and 2 == 2)

print(1 == 1 or 2 == 2)
print(1 == 2 or 2 == 2)
print(1 == 2 or 2 == 1)

print(not(1 == 2 and 2 == 2))
print(not(1 == 1 or 2 == 2))
print(not(1 == 2 or 2 == 1))

print("-" * 40)
print(ord("A"))             # integer representation of unicode character
print(ord("Z"))
print(ord("a"))
print(ord("z"))

print("apple" > "orange")
print("apple" < "orange")

print("-" * 40)
print(1 == "1")

print("Bitwise Operator".center(40, "-"))
print(f"5 | 3: {5|3}")
print(f"5 & 3: {5&3}")
print(f"5 ^ 3: {5^3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")

print(f"5 >> 1 :{5 >> 1}")
print(f"~0 :{~0}")          # -1
print(f"~5 :{~5}")          # -6

print("-" * 40)
# ternary operator
age = 12
print("Eligible" if age > 18 else "Not Eligible")
