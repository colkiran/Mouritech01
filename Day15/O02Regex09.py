
# backtracking

import re

st = "good blood bad blood"

print(f'st :{st}')

# \2 - recall the di
res = re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")