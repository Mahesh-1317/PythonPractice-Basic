list = [1,2,3,4,5]
print(list)
print(len(list))

del list[-1]
print(list)

n = int(input("Enter a number: "))
list[len(list) // 2] = n
print(list)