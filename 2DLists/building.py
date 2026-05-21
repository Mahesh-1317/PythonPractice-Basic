rooms = [[[False for r in range(20)] for r in range(15)] for b in range(3)]
print(rooms)

rooms[1][7][14] = True
rooms[1][7][4] = True
vacancy = 0
for roomNo in range(20):
    if not rooms[1][7][roomNo]:
        vacancy == 1
print("Vacancy in 3rd 15th floor of 3rd Building",vacancy)