

import re

st = "baaaaaaaat"

# res = re.search(r'ba{3}t', st)
# res = re.search(r'ba{3,}t', st)

res = re.search(r'ba{3,8}t', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found.....")