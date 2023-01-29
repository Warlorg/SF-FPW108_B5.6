def greet():
    print("|xxxxxxxxxxxxxxxxxxxx|")
    print("|  Добро пожаловать  |")
    print('|       в игру       |')
    print('|  _Крестики-нолики_ |')
    print('|        X___O       |')
    print('|<<<<<<<<<<>>>>>>>>>>|')
    print('| Введите координаты |')
    print('| А и Б через пробел,|')
    print('|  займите 3 ячейки  |')
    print('|       в ряд        |')
    print('|  или по диагонали. |')
    print('|xxxxxxxxxxxxxxxxxxxx|')


table = [[' '] * 3 for i in range(3)]


def table_output():
    print()
    print('   | 0 | 1 | 2 |')
    print('----------------')
    for i, row in enumerate(table):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print('----------------')
    print()


def request():
    while True:
        a = None
        b = None
        pos = input('Сделайте ход: ').split()
        if len(pos) != 2:
            print("Введите 2 координаты! ")
            continue
        
        if not(pos[0].isdigit() and pos[1].isdigit()):
            print("Введите числа! ")
            continue
        
        a, b = map(int, pos)
        
        if a < 0 or a > 2 or b < 0 or b > 2:
            print("Вы вышли за пределы поля! ")
            continue
        
        if table[a][b] != ' ':
            print("Ячейка занята! ")
            continue
        break
        
    return a, b


def win_rules():
    win_cond = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)))
    
    for row in win_cond:
        marks = []
        
        for i in row:
            marks.append(table[i[0]][i[1]])
            
        if marks == ['X', 'X', 'X']:
            print('Поздравляем. Выиграл Игрок №1!')
            return True
        if marks == ['O', 'O', 'O']:
            print('Поздравляем. Выиграл Игрок №2!')
            return True
    return False      


def replay():
    choice = input('Хотите сыграть снова? Да/Нет ').title()
    
    return choice == "Да"          


greet()
turn = 0
while True:
    turn += 1
           
    table_output()
    
    if turn % 2 == 1:
        player = "X"
        print("Ходит игрок №1. ")
    else:
        player = "O"
        print("Ходит игрок №2. ")
    
    x, y = request()
        
    if turn % 2 == 1:
        table[x][y] = "X"
    else:
        table[x][y] = "O"

    if turn == 9:
        table_output()
        print("Игра окончилась ничьей. ")
        turn = 0
        table = [[' '] * 3 for i in range(3)]
        replay()
        
    if win_rules():
        turn = 0
        table = [[' '] * 3 for i in range(3)]
        replay()
