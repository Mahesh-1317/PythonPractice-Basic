# 1 TO 50
# for i in range(51):
#     print(i)

# REPLACE EVEN WITH t
# for i in range(51):
#     if i%2 == 0:
#         print("t")
#     else:
#         print(i)

# QUESTION 3
for i in range(51):
    if i%3 == 0 and i%5 == 0:
        print("fizbuz")
    elif i%3 == 0:
        print("fiz")
    elif i%5 == 0:
        print("buz")
    else:
        print(i)