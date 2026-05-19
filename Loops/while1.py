largest_num = -999
num = int(input("Enter a number or type -1 to stop: "))

while num != -1:
    if num > largest_num:
        largest_num = num
    num = int(input("Enter a number or type -1 to stop: "))

print("Largest number is: ",largest_num)