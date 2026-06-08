class ExampleClass:
    a = 1
    counter = 0
    def __init__(self,val = 1):
        ExampleClass.counter += 1
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

obj = ExampleClass(3)

if hasattr(obj, 'a'):
    print("a = ",obj.a)
if hasattr(obj, 'b'):
    print("b = ",obj.b)

print(hasattr(ExampleClass, 'a'))
print(hasattr(ExampleClass, 'b'))