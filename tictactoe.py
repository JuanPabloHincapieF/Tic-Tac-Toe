board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def display_board(x):
    pretty_board = ''
    for i in range(13):
        if i == 0 or i == 4 or i == 8 or i == 12:
            pretty_board += '+' + '-'*7 + '+' + '-'*7 + '+' + '-'*7 + '+'
        elif i == 2:
            pretty_board += '|' + ' '*3 + x[0][0] + ' ' * \
                3 + '|' + ' '*3 + x[0][1] + ' ' * \
                3 + '|' + ' '*3 + x[0][2] + ' ' * \
                3 + '|'
        elif i == 6:
            pretty_board += '|' + ' '*3 + x[1][0] + ' ' * \
                3 + '|' + ' '*3 + x[1][1] + ' ' * \
                3 + '|' + ' '*3 + x[1][2] + ' ' * \
                3 + '|'
        elif i == 10:
            pretty_board += '|' + ' '*3 + x[2][0] + ' ' * \
                3 + '|' + ' '*3 + x[2][1] + ' ' * \
                3 + '|' + ' '*3 + x[2][2] + ' ' * \
                3 + '|'
        else:
            pretty_board += '|' + ' '*7 + '|' + ' '*7 + '|' + ' '*7 + '|'
        pretty_board += '\n'
    print(pretty_board)


def enter_move(x):
    while True:
        try:
            move = input('Ingresa tu movimiento: ')
            if int(move) >= 10 or int(move) <= 0:
                print('El numero que ingresaste no esta en el tablero')
            else:
                for i in range(3):
                    for j in range(3):
                        if move == x[i][j]:
                            x[i][j] = 'O'
            return display_board(x)
        except ValueError:
            print('No ingresaste un numero')
