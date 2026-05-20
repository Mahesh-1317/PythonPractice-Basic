# list = [8,10,6,2,4]
list = [2,4,6,8,10]
n = len(list)
count = 0
for i in range (n-1):
    for j in range (n-i-1):
        count += 1
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)
print(count)

# swapped = True
# count = 0
# while swapped:
#     swapped = False
#     for i in range(len(list) - 1):
#         count += 1
#         if list[i] > list[i+1]:
#             swapped = True
#             list[i],list[i+1] = list[i+1],list[i]
# print(list)
# print(count)

# list = [8,10,6,2,4]
# list.sort()
# print(list)