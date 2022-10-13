
import re

lno = 'LCNO-TEL-26-2015-0001'

res = re.search(r'LCNO-(KAR|KER|TND|TEL|APN|MAH)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})', lno)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found.....")