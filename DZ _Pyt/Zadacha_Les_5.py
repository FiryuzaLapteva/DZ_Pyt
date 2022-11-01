# 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать 
# все конфеты у своего конкурента?
# a) Добавьте игру против бота

# b) * Подумайте как наделить бота ""интеллектом""

from random import randint


print('Привет, друг, это сложная игра с простыми правила: На столе \n'
         '{K} конфет, поочереди вы с ботом берете по N-ому количеству конфет,\n' 
         'но не более 29, выигрывает тот, у кого останется 28 конфет, \n'
         'и он забирает все конфеты. Удачи.')
K = 110 # количество конфет

# Функция ввода кол-ва конфет для игрока
def user_kon(K):
    while K > 28:
        N = int(input('Введите количество конфет, которые вы хотите взять: '))
        if N <= 28:
           K = K - N 
           print(f'Осталось {K} конфет')
        if N > 28:
            print('по условия игры больше 28 конфет брать нельзя, введете соответсвующее значение')
        if K > 28:
            print(bot_kon(K)) # ход бота
        elif K < 28:
            print('Победил бот')
    
# Функция ввода кол-ва конфет для бота
def bot_kon(K):
    while K >28:
        B = randint(1,28)
        K = K - B
        print(f'бот взял {B} конфет, осталось {K} конфет')
        if K > 28:
            print(user_kon(K)) # ход игрока
        else:
            print('Победил пользователь')

#Функция жеребьевки
def ger():
    print('-----------------------------------')
    print('По итогу жеребьевки: ')
    global a
    a = randint(1,2)
    if a == 1: 
        print(f'{a} - Первый ход делает игрок')
        print('-----------------------------------\n')
        print(user_kon(K))
    else:
        print(f'{a} - Первый ход делает бот')
        print('-----------------------------------\n')
        print(bot_kon(K))
  

print(ger()) # функция жеребьевки


   

     




# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

#Прочитать данные с выбранного файла
# with open('DZ _Pyt/file1.txt', 'r') as data:
#     my_text = data.read()

# #Функция сжатия 
# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res


# # Функция восстановления данных
# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res

# print(coding(my_text))
# print(decoding(coding(my_text)))

# #Записать сжатые данные в выбранный файл
# with open('DZ _Pyt/file2.txt', 'w') as data2:
#     data2.write(coding(my_text))  


# 2. Создайте программу для игры в ""Крестики-нолики"".
# playing_field=['0','1','2','3','4','5','6','7','8'] #список с координатами игрового поля

# def printField(playing_field:list):# Функция выводящая отформатированное игровое поле
#     print(f'{playing_field[0]:^5}|{playing_field[1]:^5}|{playing_field[2]:^5}')
#     print('---------------')
#     print(f'{playing_field[3]:^5}|{playing_field[4]:^5}|{playing_field[5]:^5}')
#     print('---------------')
#     print(f'{playing_field[6]:^5}|{playing_field[7]:^5}|{playing_field[8]:^5}')

# print(printField(playing_field))

# def player_turn(playing_field:list): #функция ввода Х для игрока с проверкой на правильномть введения данных
#     while True:
#         x = int(input('Введите номер клетки для хода: '))
#         if(9>x>=0) and playing_field[x].isdigit():
#             playing_field[x]='X'
#             print(printField(playing_field))
#             break
#         else:
#             print('Клетка занята, сделайте другой ход')

# print(player_turn(playing_field))

# def player_comp(playing_field:list): #функция ввода O для игрока с проверкой на правильномть введения данных
#     while True:
#         s = int(input('Введите номер клетки для хода: '))
#         if(9>s>=0) and playing_field[s].isdigit():
#             playing_field[s]='O'
#             print(printField(playing_field))
#             break
#         else:
#             print('Клетка занята, сделайте другой ход')
# print(player_comp(playing_field))