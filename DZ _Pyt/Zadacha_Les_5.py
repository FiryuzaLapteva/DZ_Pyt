# 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать 
# все конфеты у своего конкурента?
# a) Добавьте игру против бота

# b) * Подумайте как наделить бота ""интеллектом""

from random import randint


print('\n Привет, друг, это сложная игра с простыми правила: На столе \n'
         '{K} конфет, поочереди вы с ботом берете по N-ому количеству конфет,\n' 
         'но не более 29, выигрывает тот, у кого останется 28 конфет, \n'
         'и он забирает все конфеты. Удачи.')
K = 110 # количество конфет

# Функция ввода кол-ва конфет для игрока
def user_kon(K):
        global N
        if K < 28 and K != 0:
                print('-------------------')
                print('Победил пользователь')
                print('-------------------')
        elif K > 28:
            N = int(input('Введите количество конфет, которые вы хотите взять: '))
            if N <= 28:
                K = K - N 
                print(f'Осталось {K} конфет')
                bot_kon(K) # ход бота
            if N > 28:
                print('по условия игры больше 28 конфет брать нельзя, введите соответсвующее значение')
                user_kon(K)
    
# Функция ввода кол-ва конфет для бота
def bot_kon(K):
    if a == 2: # если после жеребьевки первый ход получил бот, то
        B = K%29
        K = K - B
        print(f'бот взял {B} конфет, осталось {K} конфет')
        if K ==0:
                print('---------------')
                print('Победил бот')
                print('---------------')
        else:
            user_kon(K) # ход игрока
    elif K >=28:
        B = 29 - N
        K = K - B
        print(f'бот взял {B} конфет, осталось {K} конфет')
        if K ==0:
                print('---------------')
                print('Победил бот')
                print('---------------')
        else: 
            user_kon(K) # ход игрока
    elif K < 28 or K == 0:
        print('---------------')
        print('Победил бот')
        print('---------------')

#Функция жеребьевки
def ger():
    print('-----------------------------------')
    print('По итогу жеребьевки: ')
    global a
    a = randint(1,2)
    if a == 1: 
        print(f'{a} - Первый ход делает игрок')
        print('-----------------------------------\n')
        user_kon(K)
    else:
        print(f'{a} - Первый ход делает бот')
        print('-----------------------------------\n')
        bot_kon(K)
  

ger() # функция жеребьевки


   

     




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
# from random import randint
# playing_field=['0','1','2','3','4','5','6','7','8'] #список с координатами игрового поля

# def printField(playing_field:list):# Функция выводящая отформатированное игровое поле
#     print(f'{playing_field[0]:^5}|{playing_field[1]:^5}|{playing_field[2]:^5}')
#     print('---------------')
#     print(f'{playing_field[3]:^5}|{playing_field[4]:^5}|{playing_field[5]:^5}')
#     print('---------------')
#     print(f'{playing_field[6]:^5}|{playing_field[7]:^5}|{playing_field[8]:^5}')



# def player_human(playing_field:list): #функция ввода Х для игрока с проверкой на правильномть введения данных
#     while winner(playing_field) =='':
#         x = int(input('Игрок, введите номер клетки для хода: '))
#         if(9>x>=0) and playing_field[x].isdigit():
#             playing_field[x]='X'
#             printField(playing_field)
#             winner(playing_field)
#             if winner(playing_field) !='':
#                 print('*************\n'
#                       'Победил игрок!\n'
#                       '*************')
#                 break      
#             else:
#                 player_comp(playing_field)
#         else:
#             print('Клетка занята, сделайте другой ход')


# def player_comp(playing_field:list): #функция ввода O для игрока с проверкой на правильность введения данных
#     while True:
#         s = randint(0,9)
#         if  playing_field[s] != 'X' and playing_field[s] != 'O':
#             playing_field[s]='O'
#             print(f'Бот ввел номер клетки: {s} ')
#             printField(playing_field)
#             winner(playing_field)#Проверяем на победу
#             if winner(playing_field) !='':
#                 print('************* \n'
#                       'Победил Бот!\n'
#                       '*************')
#                 break
#             else:
#                 player_human(playing_field)
#         else:
#             print('Бот, клетка занята, сделай другой ход')


# #Функция жеребьевки
# def ger():
#     print('-----------------------------------')
#     print('По итогу жеребьевки: ')
#     global a
#     a = randint(1,2)
#     if a == 1: 
#         print(f'{a} - Первый ход делает игрок')
#         print('-----------------------------------\n')
#         player_human(playing_field)
#     else:
#         print(f'{a} - Первый ход делает бот')
#         print('-----------------------------------\n')
#         player_comp(playing_field)
  


# # Функция определения победителя

# def winner(playing_field):
#     victories = [[0,1,2], [3,4,5],[6,7,8],[0,3,6], [1,4,7], [2,5,8],[0,4,8], [2,4,6]]
#     win =''
#     for i in victories:
#         if playing_field [i[0]] == 'X'and playing_field [i[1]] == 'X'and playing_field [i[2]] == 'X':
#             win = 'X'
#         if playing_field [i[0]] == 'O'and playing_field [i[1]] == 'O'and playing_field [i[2]] == 'O':
#             win = 'O'
#     return win


# printField(playing_field)# Вывести изначальное поле игры
# ger() # функция жеребьевки
