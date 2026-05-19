# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# if n1 > n2:
#     laarger_num = n1
# else:
#     laarger_num = n2

# print("The larger number is:", laarger_num)

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
# larger_num = n1
# if n2 > larger_num:
#     larger_num = n2
# if n3 > larger_num:
#     larger_num = n3

# print("The larger number is:", larger_num)

largest_num = max(n1, n2, n3)
lowest_num = min(n1, n2, n3)
print("The largest number is:", largest_num)
print(f"{ lowest_num} is the lowest number")