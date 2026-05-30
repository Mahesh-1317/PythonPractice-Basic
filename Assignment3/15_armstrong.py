n = 153
m = n
sum = 0
while m != 0:
    ld = m % 10
    sum += ld*ld*ld  
    m //= 10
if sum == n:
    print(sum,"is a armstrong number")