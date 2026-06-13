class Level1:
    var_1 = 19
    def __init__(self):
        self.var1 = 20
    def fun_1(self):
        return 21
    
class Level2(Level1):
    var_2 = 47
    def __init__(self):
        super().__init__()
        self.var2 = 48
    def fun_2(self):
        return 49
    
class Level3(Level2):
    var_3 = 88
    def __init__(self):
        super().__init__()
        self.var3 = 99
    def fun_3(self):
        return 11
    
obj = Level3()
print(obj.var_1, obj.var1, obj.fun_1())
print(obj.var_2, obj.var2, obj.fun_2())
print(obj.var_3, obj.var3, obj.fun_3())