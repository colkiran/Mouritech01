
import re

st = "the quick brown fox jumps over the lazy dog"

res = re.search(r'(j\w+)', st)

if res:
    print("Match found....")
    print(f"Rejected String :{st[:res.start()]}")
    print(f"Regex matched string :{res.group(0)}")
    print(f"String that is yet to be checked :{st[res.end():]}")

else:
    print("Match not found.....")