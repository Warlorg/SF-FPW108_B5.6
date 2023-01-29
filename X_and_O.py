#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def greet():
    print("|xxxxxxxxxxxxxxxxxxxx|")
    print("|  Добро пожаловать  |")
    print('|       в игру       |')
    print('|  _Крестики-нолики_ |')
    print('|<<<<<<<<<<>>>>>>>>>>|')
    print('| Введите координаты |')
    print('|       А и Б,       |')
    print('|  займите 3 ячейки  |')
    print('|       в ряд        |')
    print('|  или по диагонали. |')
    print('|xxxxxxxxxxxxxxxxxxxx|')


# In[ ]:


table = [ [' '] * 3 for i in range(3)]


# In[ ]:


def table_output():
    print()
    print('   | 0 | 1 | 2 |')
    print('----------------')
    for i, row in enumerate(table):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print('----------------')
    print()
      


# In[ ]:


def request():
    while True:
        pos = input('Сделайте ход: ').split()
        if len(pos) != 2:
            print("Введите 2 координаты! ")
            continue
        
        if not(pos[0].isdigit() and pos[1].isdigit()):
            print("Введите числа! ")
            continue
        
        x, y = map(int, pos)
        
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Вы вышли за пределы поля! ")
            continue
        
        if table[x][y] != ' ':
            print("Ячейка занята! ")
            continue
        break
        
    return x, y


# In[ ]:


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
            


# In[ ]:


def replay():
    choice = input('Хотите сыграть снова? Да/Нет ').title()
    
    return choice == "Да"          


# In[ ]:


greet()
table = [ [' '] * 3 for i in range(3)]
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


# In[ ]:




