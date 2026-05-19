list = [10,20,30,40,50,60,70,80,90]
print(list)
for iterator in range(len(list)):
    list[iterator] += iterator
print(list)

list = [10,20,30,40,50,60,70,80,90]
for iterator in range(len(list)):
    list[iterator] += 1
print(list)