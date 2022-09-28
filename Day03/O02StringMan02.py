
st = "hello world"
st1 = "the quick brown fox jumps over the lazy dog"

print("replace".center(40, "-"))
print(f"st :{st}")
res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

res = st.replace("l", "L", 5)
print(f"res :{res}")

print(f"st1 :{st1}")
res = st1.replace("the", "The")
print(f"res :{res}")

res = st1.replace("the", "The", 1)
print(f"res :{res}")

print('-' * 40)
# maketrans, translate

print("maketrans".center(40, "-"))
print(f"st :{st}")

a = "helowrd"
b = 'HELOWRD'           # len(a) and len(b) should be the same
resTbl = st.maketrans(a, b)

print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")

print('-' * 40)
st = "*******hello*******"
print(f"st :{st}")

res1 = st.lstrip("*")
print(f"res1 :{res1}")

res2 = st.rstrip("*")
print(f"res2 :{res2}")

res3 = st.strip("*")
print(f"res3 :{res3}")

