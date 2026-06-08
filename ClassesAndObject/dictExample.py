class ExampleClass:
    def __init__(self,val = 1):
        self.first = val

    def set_second(self,val):
        self.second = val

object_1 = ExampleClass()
object_2 = ExampleClass(2)
object_2.set_second(3)
object_3 = ExampleClass(4)
object_3.third = 5

print(object_1)
print(object_1.__dict__)    # __dict__ USED TO PRINT OBJECT'S KEY AND VALUE IN BEAUTIFIED WAY
print(object_2.__dict__)
print(object_3.__dict__)