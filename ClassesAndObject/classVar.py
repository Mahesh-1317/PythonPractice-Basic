class ExampleClass:
    counter = 0
    def __init__(self,val = 1):
        ExampleClass.counter += 1
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

obj = ExampleClass(2)
# print(obj.a)
# print(obj.b)

try:
    print("a = ",obj.a)
except AttributeError:
    try:
        print("b = ",obj.b)
    except AttributeError:
        print("The exception is successfully handled")