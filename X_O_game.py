import copy
x_input = []
o_input = []
turns = []
field_start = [
   ['-', '-', '-'],
   ['-', '-', '-'],
   ['-', '-', '-']
]

field_play = copy.deepcopy(field_start)
xf = field_play[0]
yf = field_play[1]
zf = field_play[2]
# win comb

win_x_str = [['X', 'X', 'X'], ('Крестики в ряд')]
win_o_str = [['O', 'O', 'O'], ('Нолики в ряд')]
win_x_stolb_1 = None
win_x_stolb_2 = None
win_x_stolb_3 = None
win_x_diag_1 = None
win_x_diag_2 = None
win_o_stolb_1 = None
win_o_stolb_2 = None
win_o_stolb_3 = None
win_o_diag_1 = None
win_o_diag_2 = None

# /win comb


def print_start_field():
    index = 0
    print(" ", 0, '', 1, '', 2)
    for i in field_start:
        print(index, "  ".join(i), end='\n')
        index += 1


def print_field():
    index = 0
    print(" ", 0, '', 1, '', 2)
    for i in field_play:
        print(index, "  ".join(i), end='\n')
        index += 1


def replace_x():
    x = x_input[0]
    y = x_input[1]
    global field_play
    field_play_rep = field_play[x]
    field_play_rep.pop(y)
    field_play_rep.insert(y, 'X')


def replace_o():
    x = o_input[0]
    y = o_input[1]
    global field_play
    field_play_rep = field_play[x]
    field_play_rep.pop(y)
    field_play_rep.insert(y, 'O')


def turn_x():
    global x_input, turns
    x_input = []
    print("Ход крестиков")
    x_input.append(int(input("Введите номер строки: ")))
    x_input.append(int(input("Введите номер столбца: ")))
    print(f"Ход крестиков {x_input} - уверены?")
    des_x = input("Да/нет: ")
    if des_x == "нет":
        x_input = []
        turn_x()
    if x_input in turns:
        print("Там уже есть нолик, подумай еще!")
        turn_x()
    turns.append(x_input)


def turn_o():
    global o_input, turns
    o_input = []
    print("Ход ноликов")
    o_input.append(int(input("Введите номер строки: ")))
    o_input.append(int(input("Введите номер столбца: ")))
    print(f"Ход ноликов {o_input} - уверены?")
    des_o = input("Да/нет: ")
    if des_o == "нет":
        o_input = []
        turn_o()
    if o_input in turns:
        print("Там уже есть крестик, подумай еще!")
        turn_o()
    turns.append(o_input)


def turn__x():
    turn_x()
    replace_x()       # X - turn
    print_field()


def turn__o():
    turn_o()
    replace_o()       # O - turn
    print_field()


def end():
    answ = input("Еще разок?)\n(да/нет): ")
    if answ == 'нет':
        print("Слабак:-Р")
        exit()
    else:
        game_2()


def check_win_x():
    global win_x_str, win_x_stolb_1, win_x_stolb_2, win_x_stolb_3
    global win_x_diag_1, win_x_diag_2
    if xf[0] == 'X' and yf[0] == 'X' and zf[0] == 'X':
        win_x_stolb_1 = True
    elif xf[1] == 'X' and yf[1] == 'X' and zf[1] == 'X':
        win_x_stolb_2 = True
    elif xf[2] == 'X' and yf[2] == 'X' and zf[2] == 'X':
        win_x_stolb_3 = True
    elif xf[0] == 'X' and yf[1] == 'X' and zf[2] == 'X':
        win_x_diag_1 = True
    elif xf[2] == 'X' and yf[1] == 'X' and zf[0] == 'X':
        win_x_diag_2 = True
    if win_x_str[0] in field_play:
        print(f'Крестики выйграли!({win_x_str[1]})\nПоздравляем!')
        end()
    elif win_x_stolb_1 or win_x_stolb_2 or win_x_stolb_3:
        print(f'Крестики выйграли!(Крестики в столбик)\nПоздравляем!')
        end()
    elif win_x_diag_1 or win_x_diag_2:
        print(f'Крестики выйграли по диагонали)\nПоздравляем!')
        end()


def check_win_o():
    global win_o_str, win_o_stolb_1, win_o_stolb_2, win_o_stolb_3
    global win_o_diag_1, win_o_diag_2
    if xf[0] == 'O' and yf[0] == 'O' and zf[0] == 'O':
        win_o_stolb_1 = True
    elif xf[1] == 'O' and yf[1] == 'O' and zf[1] == 'O':
        win_o_stolb_2 = True
    elif xf[2] == 'O' and yf[2] == 'O' and zf[2] == 'O':
        win_o_stolb_3 = True
    elif xf[0] == 'O' and yf[1] == 'O' and zf[2] == 'O':
        win_o_diag_1 = True
    elif xf[2] == 'O' and yf[1] == 'O' and zf[0] == 'O':
        win_o_diag_2 = True
    if win_o_str[0] in field_play:
        print(f'Нолики выйграли!({win_o_str[1]})\nПоздравляем!')
        end()
    elif win_o_stolb_1 or win_o_stolb_2 or win_o_stolb_3:
        print(f'Нолики выйграли!(Крестики в столбик)\nПоздравляем!')
        end()
    elif win_o_diag_1 or win_o_diag_2:
        print(f'Нолики выйграли по диагонали)\nПоздравляем!')
        end()


def game():
    print("Приветствую, господа!\nПартейку в XO_Game?")
    print("Правила просты - выбираем ячейку куда хоти постаивть свой крестик или нолик.")
    print("И вводим координаты, сначала номер столбца, потом номер строки.\nПусть победит сильнейший,\nУдачи!")
    global x_input, o_input, turns, field_start, field_play, xf, yf, zf, win_x_str, win_o_str, win_o_stolb_2
    global win_x_stolb_1, win_x_stolb_2, win_x_stolb_3, win_x_diag_1, win_x_diag_2, win_o_stolb_1, win_o_stolb_3
    global win_o_diag_1, win_o_diag_2
    o_input = []
    turns = []
    field_start = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    field_play = copy.deepcopy(field_start)
    xf = field_play[0]
    yf = field_play[1]
    zf = field_play[2]
    win_x_str = [['X', 'X', 'X'], ('Крестики в ряд')]
    win_o_str = [['O', 'O', 'O'], ('Нолики в ряд')]
    win_x_stolb_1 = None
    win_x_stolb_2 = None
    win_x_stolb_3 = None
    win_x_diag_1 = None
    win_x_diag_2 = None
    win_o_stolb_1 = None
    win_o_stolb_2 = None
    win_o_stolb_3 = None
    win_o_diag_1 = None
    win_o_diag_2 = None
    print_start_field()

    turn__x()
    turn__o()

    turn__x()
    turn__o()

    turn__x()
    check_win_x()    # Third turn
    turn__o()
    check_win_o()

    turn__x()
    check_win_x()
    turn__o()
    check_win_o()

    turn__x()
    check_win_x()
    check_win_o()
    print("Ничья ¯ \ _ (ツ) _ / ¯")
    end()


def game_2():
    print("Пусть победит сильнейший!")
    global x_input, o_input, turns, field_start, field_play, xf, yf, zf, win_x_str, win_o_str, win_o_stolb_2
    global win_x_stolb_1, win_x_stolb_2, win_x_stolb_3, win_x_diag_1, win_x_diag_2, win_o_stolb_1, win_o_stolb_3
    global win_o_diag_1, win_o_diag_2
    o_input = []
    turns = []
    field_start = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    field_play = copy.deepcopy(field_start)
    xf = field_play[0]
    yf = field_play[1]
    zf = field_play[2]
    win_x_str = [['X', 'X', 'X'], ('Крестики в ряд')]
    win_o_str = [['O', 'O', 'O'], ('Нолики в ряд')]
    win_x_stolb_1 = None
    win_x_stolb_2 = None
    win_x_stolb_3 = None
    win_x_diag_1 = None
    win_x_diag_2 = None
    win_o_stolb_1 = None
    win_o_stolb_2 = None
    win_o_stolb_3 = None
    win_o_diag_1 = None
    win_o_diag_2 = None
    print_start_field()

    turn__x()
    turn__o()

    turn__x()
    turn__o()

    turn__x()
    check_win_x()    # Third turn
    turn__o()
    check_win_o()

    turn__x()
    check_win_x()
    turn__o()
    check_win_o()

    turn__x()
    check_win_x()
    check_win_o()
    print("Ничья ¯ \ _ (ツ) _ / ¯")
    end()


game()
