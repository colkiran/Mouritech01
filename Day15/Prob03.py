import re

FL = open("story.txt", "r")

cntr = 0
for line in FL.readlines():

    res = re.search(r'(\bi\w+)', line)

    if res:
        print(res.group(0))
        cntr += 1

FL.close()
print(f"There are {cntr} words starting with 'a'")