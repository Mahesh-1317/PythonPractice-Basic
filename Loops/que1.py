a = int(input("Enter a number: "))
count = 1
even = 0
odd = 0

# Count Odd and Even numbers

while count <= a:
    if count % 2 == 0:
        even += 1
    else:
        odd += 1
    
    if count == 25:
        count = 50
    count += 1

print("Odd: ",odd)
print("Even: ",even)