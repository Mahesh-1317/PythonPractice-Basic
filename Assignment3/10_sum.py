sum = 0
for i in range(1,16):
    sum += i
print(sum)

# SUM OF ALL ODD NUMBERS btw 1 TO 15
n = int(input("Enter a nuber: "))
summ = 0
for iterator in range(1,n+1):
    if iterator % 2 != 0:
        summ += iterator
print(summ)