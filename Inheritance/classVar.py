class Super:
    var1 = 1

class Sub(Super):
    var2 = 3

obj = Sub()
print(obj.var1)
print(obj.var2)