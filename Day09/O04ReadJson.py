
import json

JFR = open("books.json", "r")
jsonfile = json.load((JFR))

# print(jsonfile)
for book in jsonfile['books']:
    print(book['name'])
    print("---------")
    for k, v in book.items():
        print(k, "=>", v)
    print("=" * 40)

