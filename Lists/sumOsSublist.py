list = [1,2,3,5,7,2,8,6,4]
target = 14
for i in range (len(list)):
    cs = 0
    for j in range(i,len(list)):
        cs += list[j]
        if cs == target:
            print(list[i:j+1])