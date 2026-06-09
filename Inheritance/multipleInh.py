class SuperA:
    var1 = 10
    def fun1(self):
        return 11
    
class SuperB:
    var2 = 20
    def fun2(self):
        return 21
    
class Sub(SuperA, SuperB):
    pass

obj = Sub()
print(obj.var1, obj.fun2())
print(obj.var2, obj.fun1())