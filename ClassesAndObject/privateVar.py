class Python:
    population = 1000
    victim = 0
    def __init__(self):
        self.length = 3
        self.__venomous = False

myObj = Python()
print("Population: ",myObj.population)
print("Victim: ",myObj.victim)
print("Length: ",myObj.length)
# print("Venomous: ",myObj.__venomous)    #PRIVATE VARIABLE
print("Venomous:",myObj._Python__venomous)      #ACCESS PRIVATE VARIABLE

print(hasattr(Python,'constructor'))