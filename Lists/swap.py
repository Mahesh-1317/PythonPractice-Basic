a = 4
b = 5

# c = a
# a = b
# b = c

a,b = b,a
print("a = ",a,"b = ",b)

list = [1,2,3,4,5,6]
print(list)
list[0],list[5]= list[5],list[0]
print(list)