
import re

st = "the quick brown fox jumps over the lazy dog"

print(F"st :{st}")

res = re.sub('t\w+', "The", st, 1)

print(f"res :{res}")
