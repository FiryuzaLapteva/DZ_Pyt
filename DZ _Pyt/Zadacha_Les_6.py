# 32. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint

# list1 = [randint(0, 10) for i in range(10)]
# list2= [i for i in list1 if list1.count(i)==1]

# print(list1)
# print(list2)

# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, 
# а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: 
# одна строка — один пользователь. Написать код, загружающий данные из обоих 
# файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.

# Сохранить словарь в файл users_hobby.txt.

# keys = open('DZ _Pyt/user.txt', encoding='utf8').read().split('\n')
# values = open('DZ _Pyt/hobby.txt', encoding='utf8').read().split('\n')
# info = dict(zip(keys, values))
# print(info)

# import json
# with open('DZ _Pyt/users_hobby.txt', 'w') as data:
#     data.write(json.dumps(info))

