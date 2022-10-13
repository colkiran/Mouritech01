
class MyListClass(list):

    def append(self, object):
        print("Record :", object)
        super().append(object)

    def pop(self, ind):
        pass

    def extend(self, itr):
        pass

l1 = MyListClass()
print(f"l1 :{l1}")
print(type(l1))

l1.append("Sachin")
l1.append("Sourav")
l1.append("Rahul")

print(l1)

