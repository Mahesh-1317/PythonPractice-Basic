# def list_sum(lst):
#     s = 0
#     for i in lst:
#         s += i
#     return s
# print(list_sum([4,2,2]))

def list_fun(n):
    list =[]
    for i in range(0,n):
        list.insert(0,i)
        #list.append(i+1)
    return list
print(list_fun(6))