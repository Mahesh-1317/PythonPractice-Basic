board = []
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
# print(board)

# for i in board:
#     print([i])
# print(len(board))

# P = "PAWN"
# R = "ROOKS"
# K = "KNIGHT"
# B = "BISHAP"
# Q = "QUEEN"
# k = "KING"       

board[0][0] = "Rooks"
board[0][7] = "Rooks"
board[7][0] = "Rooks"
board[7][7] = "Rooks"

board[0][3] = "King"
board[7][3] = "King"

board[0][4] = "Queen"
board[7][4] = "Queen"

board[0][1] = "Knights"
board[0][6] = "Knights"
board[7][1] = "Knights"
board[7][6] = "Knights"

board[0][2] = "Bishap"
board[0][5] = "Bishap"
board[7][2] = "Bishap"
board[7][5] = "Bishap" 

for i in board:
    print([i])