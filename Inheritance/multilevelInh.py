class Level1:
    var = 10
    def fun(self):
        return 11
    
class Level2(Level1):
    var = 20                # Overrides Level1.var
    def fun(self):          # Overrides Level1.fun()            # BECAUSE PYTHON FOLLOWS BOTTOM TO TOP APPROACH
        return 21
    
class Level3(Level2):
    pass

obj = Level3()
print(obj.var, obj.fun())