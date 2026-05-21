list = []
# for i in range(24):
#     row = ["0.0" for i in range(31)]
#     board.append(row)

temp =[[0.0 for h in range(24)] for d in range(31)] 

temp1 = 20
temp2 = 15
count = 0

for day in temp:
    if count == 0:
        day[11] = temp1
        count = 1
    else:
        day[11] = temp2
        count = 0

for element in temp:
    print(element)

total = 0.0
for day in temp:
    total += day[11]
average = total / 31

for i in temp:
    print(i)
print("Average: ",average)

max_temp = -100.0
for day in temp:
    for hourly_temp in day:
        if hourly_temp > max_temp:
            max_temp = hourly_temp
print("Max temperature:", max_temp)

hotDays = 0
for d in temp:
    if d[11] > 15.0:
        hotDays += 1
print(hotDays, "were hot days")