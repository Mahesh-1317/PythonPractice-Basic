x = ["Maruti", "BMW"]
y = ["Maruti", "BMW"]
Z = x
print(x is y)
print(x is Z)
print(y is Z)

p = "Curvv"
print(p in x)
print(p not in x)

name = input("Enter your name: ")
print("Hello, " + name)

print("\n")

x = input("Enter a number: ")
y = input("Enter another number: ")
z = x + y
print("Sum:", z)

z = int(x) + int(y)
print("Sum after converting to integers:", z)