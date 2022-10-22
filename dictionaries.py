#
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for country in capitals.keys():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
#     print(country)



# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for capital in capitals.values():     # итерируем по списку ['Москва', 'Париж', 'Прага']
#     print(capital)


# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for item in capitals.items():
#     print(item)



# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key, value in capitals.items():
#     print(key, '-', value)



#
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# print(*capitals, sep='\n')  # распаковка ключей словаря


'''
Сортировка по ключам выполняется с использованием функции sorted().
'''

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
#
# for key in sorted(capitals, reverse=False):
#     print(key)

'''
Для сортировки словаря по значениям можно использовать функцию sorted() вместе с методом items().
'''


# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
#
# for key, value in sorted(capitals.items(), key = lambda x: x[1]):
#     print(value)



# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Россия' in capitals:
#     print('В словаре есть ключ Россия')


# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# if 'Париж' in capitals.values():
#     print('В словаре есть значение Париж')



'''
Решим следующую задачу: пусть задан список чисел numbers, где некоторые числа встречаются неоднократно. Нужно узнать, сколько именно раз встречается каждое из чисел.
'''

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# # ???
# result = {}
# for num in numbers:
#     result[num] += 1

# {9: 2, 32: 5... }

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result.keys():
#         result[num] = 1
#     else:
#         result[num] += 1
#
# print(result)


# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# print(info['name'])


# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# print(info['salary']) # ошибка



# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# item1 = info.get('salary')
# item2 = info.get('salary', 'Информации о зарплате нет') # значение, которое вернется, если заданного ключа нет
#
# print(item1)
# print(item2)


# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# print(result)



'''
Метод update() – реализует своеобразную операцию конкатенации для словарей. 
Он объединяет ключи и значения одного словаря с ключами и значениями другого. 
При совпадении ключей в итоге сохранится значение словаря, указанного в качестве аргумента метода update().
'''


# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
#
# info1.update(info2)
#
# print(info1)



# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
#
# info1 |= info2
#
# print(info1)



'''
Метод setdefault() позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря, если он отсутствует
key: ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать.
default: значение, которое будет использовано при добавлении нового элемента в словарь.
В зависимости от значений параметров key и default возможны следующие сценарии работы данного метода.

Сценарий 1. Если ключ key присутствует в словаре, то метод возвращает значение по заданному ключу (независимо от того, передан параметр default или нет).
Сценарий 2. Если ключ key отсутствует в словаре, то метод вставляет переданное значение default по заданному ключу.
'''

# info = {'name': 'Bob',
#         'age': 25}
#
# name1 = info.setdefault('name')           # параметр default не задан
# name2 = info.setdefault('name', 'Max')    # параметр default задан
#
# print(name1)
# print(name2)



# info = {'name': 'Bob',
#         'age': 25}
#
# job = info.setdefault('job', 'Dev')
# print(info)
# print(job)




# info = {'name': 'Bob',
#         'age': 25}
#
# job = info.setdefault('job') # параметр default не задан
# print(info)
# print(job)


'''
С помощью оператора del можно удалять элементы словаря по определенному ключу.
'''



# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher',
#         'email': 'timyr-guev@yandex.ru'}
#
# del info['email']    # удаляем элемент имеющий ключ email
# del info['job']      # удаляем элемент имеющий ключ job
#
# print(info)


'''
Оператор del удаляет из словаря элемент по заданному ключу вместе с его значением. 
Если требуется получить само значение удаляемого элемента, то нужен метод pop().
'''

#
# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher',
#         'email': 'samv@yandex.ru'}
#
# email = info.pop('email')          # удаляем элемент по ключу email, возвращая его значение
# job = info.pop('job')              # удаляем элемент по ключу job, возвращая его значение
#
# print(email)
# print(job)
# print(info)


'''
Чтобы ошибка не появлялась, этому методу можно передать второй аргумент. 
Он будет возвращен, если указанного ключа в словаре нет. Это позволяет реализовать безопасное удаление элемента из словаря:
'''

# surname = info.pop('surname', None)


'''
Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение).
'''


# info = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
#
# info['surname'] = 'Sinclar'
#
# item = info.popitem()
#
# print(item)
# print(info)



'''
Метод clear() удаляет все элементы из словаря.
'''

#
# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info.clear()
#
# print(info)


'''
Метод copy() создает поверхностную копию словаря.
'''
#
# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# new_info = info
# new_info['name'] = 'Tim'
#
# print(info)


# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# new_info = info.copy()
# new_info['name'] = 'Tim'
#
# print(info)
# print(new_info)

'''
Словарь можно использовать вместо нескольких вложенных условий, если вам нужно проверить число на равенство. Например вместо
'''

# num = int(input('Введите число: '))
#
# if num == 1:
#     description = 'One'
# elif num == 2:
#     description = 'Two'
# elif num == 3:
#     description = 'Three'
# else:
#     description = 'Unknown'
#
# print(description)


# num = int(input('Введите число: '))
#
# description = {1: 'One', 2: 'Two', 3: 'Three'}
#
# print(description.get(num, 'Unknown'))



# keys = ['name', 'age', 'job']
# values = ['Ivan', 28, 'Teacher', 23]
#
# info = dict(zip(keys, values))
#
# print(info)