# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, 
# а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: 
# одна строка — один пользователь. Написать код, загружающий данные из обоих 
# файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.

# Сохранить словарь в файл users_hobby.txt. 

# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи


# keys = open('DZ _Pyt/user.txt').read().split('\n')
# values = open('DZ _Pyt/hobby.txt').read().split('\n')
# info = dict(zip(keys, values))
# print(info)

# import json
# open('DZ _Pyt/users_hobby.txt', 'w').write(json.dumps(info))


# 31. Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.


# N = int(input('Введите целое положительное число '))
# def factor(num):
#     my_list = list()
#     m=2
#     while(m<=num):
#         if (num%m) == 0:
#             my_list.append(m)
#             num = num/m
#         else:
#             m +=1
#     return my_list
          
# print(factor(N))      

# 32. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint, random
# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 10))# заполняем список list рандомно числами от 0 до 10
# print(f'Исходная последовательность чисел {list}')

# list2 = []
# for i in list:
#     if list.count(i)==1:
#         list2.append(i)
# print(list2)

# короткое решение 
# list1 = [randint(0, 10) for i in range(10)]
# print(list1)
# list2= [i for i in list1 if list1.count(i)==1]
# print(list2)

# 33. Задана натуральная степень k. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

# from random import randint
# import itertools # принимает несколько итераций и возвращет одну последовательность

# k = int(input('Введите натуральную степень k:'))
# def get_koeff(k): 
#     koeff = [randint(0, 100) for i in range (k + 1)]
#     while koeff[0] == 0:
#         koeff[0] = randint(1, 100)
#         # коэфф. при старшей степени не должен быть равен 0 
#     return koeff

# def get_polynomial(k, koeff):
#     var = ['x^']*(k-1) + ['x']
#     # (k-1) - кол-во повторений [*x^]
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(koeff, var, range(k, 1, -1),
#     fillvalue = '') if a !=0]
#     # itertools.zip_longest(*iterables, fillvalue=None) fillvalue - пропущенные элементы
#     print (polynomial)
#     for x in polynomial:
#         x.append(' + ')
#     print(polynomial)
#     polynomial = list(itertools.chain(*polynomial))
#     # itertools.chain Создаёт итератор представляющий единой цепочкой элементы указанных объектов.
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# koeff = get_koeff(k)
# polynom1 = get_polynomial(k, koeff)
# print(polynom1)

# with open('DZ _Pyt/Polynomial_1.txt', 'w') as data:
#     data.write(polynom1)


# 34. *Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
# from dataclasses import replace
# import re


# poly_1 = open('DZ _Pyt/Polynomial_1.txt').read().split('+')
# print(poly_1)

# poly_2 = open('DZ _Pyt/Polynomial_2.txt').read().split ('+')
# print(poly_2)


# def koeff(my_list):
#     for i in my_list:
#         z = list(re.findall(r'[\d+\.\-\+]+',i))
#         res=(list(map(int, z)))
#         myDict = {res[0]: res[i] for i in range(0, len(res), 1)} 
#         print(list(myDict))# Список по ключам

   
# print(koeff(poly_1))
# print(koeff(poly_2))





# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0
