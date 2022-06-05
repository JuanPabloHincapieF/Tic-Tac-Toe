board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

x = input('numero: ')

for i in range(3):
    for j in range(3):
        if x == board[i][j]:
            board[i][j] = 'X'
print(board)
