#Operators

a = 10
b = 5

a>>=1
print("a>>=1:",a)  # Right shift assignment
b<<=1
print("b<<=1:",b)  # Left shift assignment
a&=1
print("a&=1:",a)    # Bitwise AND assignment

print(b<5 and b>3)
print(b<5 or b>3)
print(not(b<5 and b>3))

print(a is b)
print(a is not b)