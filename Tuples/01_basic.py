# tuple = (1,10,100)
# t1 = tuple + (9,99)
# t2 = tuple * 3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in tuple)
# print(9 not in tuple)

t1 = (1,2,3)
for i in t1:
    print(i)

t2 = (1,2,3,4)
print(5 in t2)
print(5 not in t2)

t3 = (1,2,3,4)
print(len(t3))

t4 = t1 + t2
t5 = t3 * 2
print(t4)
print(t5)