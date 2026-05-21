rooms = [[[False for r in range(20)] for r in range(15)] for b in range(3)]
for i in rooms:
    print(i)
# print(rooms)

rooms[1][9][13] = True
rooms[0][4][1] = False
vacancy = 0
for roomNo in range(20):
    if not rooms[2][14][roomNo]:
        vacancy == 1
print(vacancy)