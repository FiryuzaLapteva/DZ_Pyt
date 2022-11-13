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

# 38. Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# print(del_some_words(my_text))


#  42. Есть список чисел. Вывести – является ли последовательность строго убывающей, 
# или строго возрастающей, или ни то, ни другое

# from operator import sub

# my_list = [6, 5, 4, 3, 2, 1]
# list2 = my_list.copy()# Создаем копию списка my_list
# del list2[0] #Удаляем элемент под индексом [0]

# sub_iter = list(map(sub, list2, my_list)) #Вычитаем итерационно список list2 из my_list
# print (list(sub_iter))

# if sub_iter[0] == 1 and len(sub_iter) == sub_iter.count(sub_iter[0]):
#     print('Возрастающая')
# if sub_iter[0] == -1 and len(sub_iter) == sub_iter.count(sub_iter[0]):
#     print('Убывающая')
# else:
#     print('Ни то, ни то')

