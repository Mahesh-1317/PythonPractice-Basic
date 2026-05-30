str = "UraanSoftskills"
# repeat = []
# unique = []
# for i in str:
#     if str.count(i) > 1:
#         if i not in unique:
#             repeat.append(i)
#     else:
#         unique.append(i)
# print("Repeated: ",repeat)
# print("Unique: ",unique)
# print(len(repeat))
# print(len(unique))

repeat = 0
unique = 0
for i in str:
    if str.count(i) > 1:
        repeat += 1
    else:
        unique += 1
print("Repeated: ",repeat)
print("Unique: ",unique)