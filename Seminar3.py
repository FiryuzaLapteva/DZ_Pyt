# работа с файлами:
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+
# r+ 

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')# 'a'- мод для добавления данных 
# #w - для записи данных, данные будут перезаписаны(старые данные удаляются)
# data.writelines(colors) #Записать набор данных, разделителей не будет
# data.write('\n Line 2 \n' )
# data.write('\n Line 3 \n' )

# data.close()# Обязательно закрыть файл во избежания утечек памяти

# with open('file.txt', 'w') as data:
#     data.write('line 123 \n')
#     data.write('line 321 \n')
    # В данной записи происходит автоматический разрыв файла с переменной data

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

#Обращение к функциям из других файлов
# import Seminar1 as S1 #Импортируем файл, для короткой записи можем присвоить новое имя файлу более короткое
# print(S1.f(1)) #Обращаемся к файлу, вызываем функцию и вставляем данные

# def new_string(symbol, count = 3): # функция - название придумываем, в скобках - переменные
#     return symbol * count
#     # мы сразу count присвоили значение 3
# print(new_string('!', 3)) #!!!
# print(new_string('!')) #!!! сразу выводт 3 раза !
# print(new_string(4)) #12  Python распознает 4 как число, поэтому происходит операция умножения 4 * 3

# def concatenetion(*params): # * неограниченное кол-во элементов
#     res: str = "" # результат - строка, если введем числа - ошибка
#     for item in params:
#         res += item #Склеиваем строки
#     return res
# print(concatenetion('a' 's' 'd')) 

# def fib (n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib (n-1) + (n-2)
# list = []
# for e in range(1,10):
#     list.append(fib, list, e)
# print(list)


#МНОЖЕСТВЕННОЕ ПРИСВАИВАНИЕ
# a, b = 3, 4

# #КОРТЕЖ (TUPLE) - НЕИЗМЕНЯЕНЫЙ "СПИСОК"
# (a) = (3, 4)
# print(a)
# print(a[1])
# a[0]=12 # не работает для КОРТЕЖЕЙ/ СПИСОК ЭЛЕМЕНТОВ ОСТАЕТСЯ ВСЕГДА НЕИЗМЕННЫЙ

#СЛОВАРИ - НЕУПОРЯДОЧНЫЕ КОЛЛЕКЦИИ ПРОИЗВОЛЬНЫХ ОБЪЕКТОВ С ДОСТУПОМ ПО КЛЮЧУ


# 19. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# 20.  Вывести список, содержащий средние арифметические значения чисел каждого 
# вложенного кортежа в заданном кортеже кортежей numbers.
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# 21. Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1



# number = input ('Введите искомые символы ')
# my_list = ['сыр', '123', 'привет']
# flag = False
# for i in my_list:
#     if i == number:
#         flag = True
#         print(f'{number}  есть в  списке') 
# if flag == False:
#       print(f'{number}  нет списке')  

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# my_list = []
# for i in numbers:
#     my_list.append(sum(i)/len(i))
# print(my_list)

# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# my_string = 'qwe'
# if my_string in my_list:
#     a = my_list.index(my_string)
#     for i in range(a+1,len(my_list)):
#         if my_list[i] == my_string:
#             print(i)
#             break
#         else:
#             print('-1')
# else:
#     print('-1')

# 27. Задайте строку из набора чисел. Запишите ее в файл. 
# Напишите программу, которая считает строку из файла и покажет большее и меньшее число.
#  В качестве символа-разделителя используйте пробел.
# from ctypes import util


# str1 = '1, 2, 34, 68'
# with open('file.txt', 'w' ) as data:
#     data.write(str1)
# with open('file.txt') as data:
#     str2 = data.read()
#     print(data.read)
# print(str2.split(', '))
# my_list = []
# for el in str2.split(', '):
#     my_list.append(int(el))
# print(max(my_list), min(my_list))

    


# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python
# При этом функцию для нахождения дискриминанта импортируйте из файла utils.py

# A = 1
# B = -8
# C = 12

# from utils import ds
# from math import sqrt
# x1 = (-B-(sqrt(ds(A, B, C))))/2*A
# x2 = (-B+ sqrt(ds(A, B, C)))/2*A

# # x1 = round((-B + sqrt(ds))/2 * A,2)
# # x2 = round((-B - sqrt(ds))/2 * A,2)

# print(x1, x2)





# 29 .Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# def Letter(elem):
#    return elem[0] == 'i'

# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# print(list(filter(Letter,products)))


