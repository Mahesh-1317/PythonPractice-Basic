# t = tuple((1,2,"string"))
# print(t)
# print(type(t))

# list = [2,4,5]
# print(list)
# print(type(list))

# tup = tuple(list)
# print(tup)
# print(type(tup))

var = 123
t1 = (1,)
t2 = (2,)
t3 = (3,var)
t1,t2,t3 = t2,t3,t1
print(t1,t3,t2)