
"""
1. between b and t there can be any alphabet in lower case
"""


import re

st = "bdt"
# res = re.search(r'b[a-zA-Z0-9]t', st)
# res = re.search(r'b[aeiuo]t', st)

res = re.search(r'b[^aeiuo]t', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found.....")