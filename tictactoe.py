from random import randrange
import textos
board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]


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
            return x
        except ValueError:
            print('No ingresaste un numero')


# implementar list_fields


def list_fields(x):
    vacios = []
    for i in range(3):
        for j in range(3):
            if x[i][j] == 'O' or x[i][j] == 'X':
                continue
            else:
                aux = [i, j]
                vacios.append(tuple(aux))

    return vacios


def draw_move(x):
    while True:
        rdm = str(randrange(1, 10))
        for i in range(3):
            for j in range(3):
                if rdm == x[i][j]:
                    x[i][j] = 'X'
                    return display_board(x)
                else:
                    continue


def game(x):
    display_board(x)
    for f in range(4):
        enter_move(x)
        for i in range(3):
            if x[0][i] == 'O' and x[1][i] == 'O' and x[2][i] == 'O':
                return textos.ganaste

            elif x[0][i] == 'X' and x[1][i] == 'X' and x[2][i] == 'X':
                return textos.perdiste
            else:
                continue

        for i in range(3):
            if x[i][0] == 'O' and x[i][1] == 'O' and x[i][2] == 'O':
                return textos.ganaste
            elif x[i][0] == 'X' and x[i][1] == 'X' and x[i][2] == 'X':
                return textos.perdiste
            elif x[0][0] == 'X' and x[1][1] == 'X' and x[2][2] == 'X':
                return textos.perdiste
            elif x[0][2] == 'X' and x[1][1] == 'X' and x[2][0] == 'X':
                return textos.perdiste
            else:
                continue
        draw_move(x)
        for i in range(3):
            if x[0][i] == 'O' and x[1][i] == 'O' and x[2][i] == 'O':
                return textos.ganaste
            elif x[0][i] == 'X' and x[1][i] == 'X' and x[2][i] == 'X':
                return textos.perdiste
            else:
                continue

        for i in range(3):
            if x[i][0] == 'O' and x[i][1] == 'O' and x[i][2] == 'O':
                return textos.ganaste
            elif x[i][0] == 'X' and x[i][1] == 'X' and x[i][2] == 'X':
                return textos.perdiste
            elif x[0][0] == 'X' and x[1][1] == 'X' and x[2][2] == 'X':
                return textos.perdiste
            elif x[0][2] == 'X' and x[1][1] == 'X' and x[2][0] == 'X':
                return textos.perdiste
            else:
                continue
    return textos.empate


print(game(board))
