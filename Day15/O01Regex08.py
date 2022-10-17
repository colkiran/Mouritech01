
import re

st = "this is a samplee ample string"

print(f"st :{st}")
# res = re.search(r'\w+', st)
# res = re.search(r'\W+', st)
# res = re.search(r'\d+', st)
# res = re.search(r'\D+', st)
# res = re.search(r'\s+', st)
# res = re.search(r'(\ba\w+)', st)
# res = re.search(r'(\Ba\w+)', st)

res = re.search(r'(\Athis)', st)

if res:
    print("Match found")
    print(res.group(0))
else:
    print("Match not found")