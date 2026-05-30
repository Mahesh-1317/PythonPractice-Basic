str = "UraanSoftskills"
str2 = ""
count = 0
for i in str:
    if i not in str2:
        count = 0
        for j in str:
            if i == j:
                count += 1
        print(i," = ", count)
        str2 += i