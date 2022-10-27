playing_field=['0','1','2','3','4','5','6','7','8'] #список с координатами игрового поля

def printField(playing_field:list):# Функция выводящая отформатированное игровое поле
    print(f'{playing_field[0]:^5}|{playing_field[1]:^5}|{playing_field[2]:^5}')
    print('---------------')
    print(f'{playing_field[3]:^5}|{playing_field[4]:^5}|{playing_field[5]:^5}')
    print('---------------')
    print(f'{playing_field[6]:^5}|{playing_field[7]:^5}|{playing_field[8]:^5}')

print(printField(playing_field))

def player_turn(playing_field:list): #функция ввода Х для игрока с проверкой на правильномть введения данных
    while True:
        x = int(input('Введите номер клетки для хода: '))
        if(9>x>=0) and playing_field[x].isdigit():
            playing_field[x]='X'
            print(printField(playing_field))
            break
        else:
            print('Клетка занята, сделайте другой ход')

print(player_turn(playing_field))

def player_comp(playing_field:list): #функция ввода O для игрока с проверкой на правильномть введения данных
    while True:
        s = int(input('Введите номер клетки для хода: '))
        if(9>s>=0) and playing_field[s].isdigit():
            playing_field[s]='O'
            print(printField(playing_field))
            break
        else:
            print('Клетка занята, сделайте другой ход')

print(player_comp(playing_field))