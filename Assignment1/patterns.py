#Hollow Square or rectangle

# print("*"*6)
# print(("*" + " "*4 + "*\n")*4,end=" ")
# print("*"*6)

# print("*"*6)
# for i in range(4):
#     print("*    *")
# print("*"*6)

# i = 1
# print("*"*6)
# while i <= 4:
#     print("*    *")
#     i += 1
# print("*"*6)

# FILLED SQUARE

# print(("#" + "#"*6 + "#\n")*6,end=" ")

# for i in range(6):
#     print("#"*8)

n = 6
for i in range (1,n+1):
    for j in range (n-1):
        print("#",end=" ")
    print("#")