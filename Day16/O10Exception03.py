
# l1 = [1, 2, 3]
# l2 = [3, 2, 1]
#
# print(l1 != l2)
# print(l1 > l2)
# print(l1 < l2)
import logging

logging.basicConfig(level=logging.WARNING)

class lst1_GT_lst2(Exception):
    pass

class lst2_LT_lst1(Exception):
    pass

l1 = list(range(1, 6))
l2 = list(range(1, 5))

try:
    if l1 == l2:
        print(f"Both lists are equal :{l1} \t {l2}")

    if l1 > l2:
        raise lst1_GT_lst2(logging.error("list1 is greater than list2"))

    if l2 > l1:
        raise lst2_LT_lst1(logging.critical("list2 is greater than list1"))

except lst1_GT_lst2 as L1:
    print(L1)
except lst2_LT_lst1 as L2:
    print(L2)

finally:
    print("list comparison completed.......")