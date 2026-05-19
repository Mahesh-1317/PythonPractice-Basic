blocks = int(input("Enter the number of blocks: "))
height = 0
layer = 0

while layer <= blocks:
    height += 1
    blocks -= 1
    layer += 1
print("The height of the pyramid:", height)
print("Layer: ",layer)