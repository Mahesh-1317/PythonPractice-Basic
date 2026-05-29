# class Student:
#     def __init__(self):          #INITIALIZING METHOD CALLED CONSTRUCTOR
#         self.name = ""
#         self.age = 0
#         self.gender = ""

# thanos = Student()
# print(thanos)

# thanos.name = "Mahamanav Thanos"
# thanos.age = 517
# thanos.gender = "Male"

# print(thanos.name)
# print(thanos.age)
# print(thanos.gender)

class Student:
    def __init__(self,name,age,gender):          #INITIALIZING METHOD CALLED CONSTRUCTOR
        self.name = name
        self.age = age
        self.gender = gender

    def printDetails(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)

alien = Student("Mahamanav Thanos", 517, "Male")
print(alien)

alien.printDetails()