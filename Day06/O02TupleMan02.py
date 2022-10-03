
from collections import namedtuple

nmdTpl = namedtuple("Products", "pname price qty cat")
prod = nmdTpl(pname= "Pepsi", price=90, qty=3, cat="Baverage")
print(prod)

print(f"Prod Name     :{prod.pname}")
print(f"Prod Price    :{prod.price}")
print(f"Prod Qty      :{prod.qty}")
print(f"prod category :{prod.cat}")

prod.pname = "Coke"
