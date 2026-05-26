# def message():
#     print("Enter a value: ")

# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())

# print(message)

# def message():
#     print("Enter a value: ")
#     num = int(input())
#     return num
# a = message()
# b = message()
# print("a: ",a,"b: ",b)

# PARAMETERIZED FUNCTION

# def hello(n):
#     print("Hello,",n)
# name = input("Enter your name: ")
# hello(name)

# def fun(num):
#     print("Number: ",num)
# num = 457
# fun(2)
# print(num)

# def message(what,number):
#     print("Enter",what,"number: ",number)
# message("roll",101)

# def intro(first_name,last_name):
#     print("Hello, my name is",first_name,last_name)
# intro("Peter","Parkar")
# intro(first_name="Aditya",last_name="Gupta")

# def add(a,b,c):
#     print(a, "+", b, "+", c, "=",a+b+c)
# add(1,2,4)
# add(c=1,a=2,b=4)
# add(1,c=2,b=4)
# #add(1,a = 2,b = 4)  ERROR

# def new_year(wishes = True):
#     print("Three...")
#     print('Two...')
#     print("One...")
#     if not wishes:
#         return
#     print("Happy new year!")
# new_year(True)
# new_year(False)

# def boring_fun():
#     print("Boring")
#     return 123
# print("This lesson is")
# boring_fun()

# def checkMyVar(var):
#     if(var == 10):
#         print("Variable is 10")
#         return 1
#     else:
#         print("Variable is not up to the mark")
#         return
# print(checkMyVar(10))
# checkMyVar(5)
# print(checkMyVar(5))  

#   FUNCTION SCOPE

# def scope_test():
#     x = 12
# scope_test()
# print(x)    # ERROR

# def fun():
#     print("Do I know that variable?",var)
# var = 1
# fun()
# print(var)

# def mul(x):
#     var = 7
#     return x * var
# var = 3
# print(mul(7))

# def fun():
#     global var
#     var = 2 
#     print("Variable: ",var)
# var  =1
# fun()
# print(var)

# var = 2
# print(var)
# def return_var():
#     global var
#     var = 5
#     return var
# print(return_var())
# print(var)

# def myFun(n):
#     print("I got",n)
#     n += 1 
#     print("I have",n)
# var = 1
# myFun(var)
# print(var)

# def list_fun(list1):
#     print("Print 1: ",list1)
#     print("Print 2: ",list2)
#     list1 = [0,1]
#     print("Print 3: ",list1)
#     print("Print 4: ",list2)

# list2 = [2,3]
# list_fun(list2)
# print("Print 5: ",list2)

def list_fun(list1):
    print("Print 1: ",list1)
    print("Print 2: ",list2)
    del list1[0]
    print("Print 3: ",list1)
    print("Print 4: ",list2)
                                # ASSIGN = NOT AAFFECT (NOT MUTABLE)  
list2 = [2,3]       # DELETION WORK ON BOTH REFERENCES (GLOBAL AND LOCAL)
list_fun(list2)
print("Print 5: ",list2)