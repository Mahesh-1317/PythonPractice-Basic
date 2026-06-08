class Sample:
    def __init__(self,val):
        self.val = val

obj1 = Sample(0)
obj2 = Sample(2)
obj3 = obj1
obj3.val += 1

print(obj1 is obj2)
print(obj2 is obj3)
print(obj3 is obj1)
print(obj1.val,obj2.val,obj3.val)

str1 = "Mary has a little "
str2 = "Mary has a little lamb"
str1 += "lamb"

print(str1 == str2, str1 is str2)