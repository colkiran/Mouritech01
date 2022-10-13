

import re

st = "the quick brown fox jumps over the lazy dog"

# res = re.match(r'^the', st)

# match can only search at the beginning of the string

res = re.search(r'dog$', st)

if res:
    print("Match found....")
    print(res.group(0))                 # string that matched our regex
else:
    print("Match not found.....")