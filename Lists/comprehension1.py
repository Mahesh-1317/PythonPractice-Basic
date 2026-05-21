# list = []
# for i in range (8):
#     list.append("WHITE_PAWN")

list = ["WHITE_PAWN" for i in range(8)]  # LIST COMPREHENSION
print(list)

square = [n ** 2 for n in range(1,11)]
print(square)

odds = [x for x in square if x % 2 != 0]
print(odds)

twos = [2 ** i for i in range(8)]
print(twos)