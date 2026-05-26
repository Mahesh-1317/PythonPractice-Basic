# def num(n):
#     print(n)
#     if n == 0:
#         return
#     else:
#         num(n-1)
# num(5)

def fact(n):
    if n <= 1:
        return 1
    else:
        return n* fact(n-1)
print(fact(5))      