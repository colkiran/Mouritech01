
width = 50
price_width = 10
item_width = width - price_width

header_fmt = "{{:{}}}{{:>{}}}".format(item_width, price_width)
fmt = "{{:{}}}{{:>{}.2f}}".format(item_width, price_width)
print("=" * width)
print(header_fmt.format("Item", "Price"))
print("=" * width)

print(fmt.format("Apples", 0.4))
print(fmt.format("Pears", 0.5))
print(fmt.format("Cantaloupes", 1.92))
print(fmt.format("Dried Apricots (16 oz.)", 8))
print(fmt.format("Prunes (4 lbs.)", 12 ))
print("=" * width)



# print("="*50)
# print("{name:<40} {price}".format(name = "Item", price = "Price"))
# print("="*50)
# print("{name:<40} {price}".format(name = "Apples", price = "0.40"))
# print("{name:<40} {price}".format(name = "Pears", price = "0.50"))
# print("{name:<40} {price}".format(name = "Cantaloupes", price = "1.92"))
# print("{name:<40} {price}".format(name = "Dried Apricots (16 oz.)", price = "8.00"))
# print("{name:<40} {price}".format(name = "Prunes (4 lbs.)", price = "12.00"))
# print("="*50)