'''
Функция filter(func, *iterables) принимает первым аргументом функцию, которая должна возвращать True или
False для своего аргумента. Второй аргумент — любая последовательность (iterable).
'''

# def func(elem):
#     return elem >= 0
#
#
# numbers = [-1, 2, -3, 4, 0, -20, 10]
# positive_numbers = list(filter(func, numbers))
#
# print(positive_numbers)




'''
В качестве func можно использовать и методы классов:
'''
# nums = ['0', 'Samsung Galaxy', '15.5', '18,1', 'iPhone', '748', 'HelloWord']
# int_nums = list(filter(str.isalpha, nums))
# print(int_nums)

'''
ЗАДАЧА
У нас есть список товаров и необходимо выбрать некоторые из них по заданному
критерию — например, на букву ‘i’
'''

# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# def Letter(elem):
#    return elem[0] == 'i'
#
# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# print(list(filter(Letter,products)))








#
#
#
#
#
#
#
#
#
#
#
#
#

# products = ['IPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# def accepted(el):
#     return el.lower().startswith('i')
#
# products_sample = filter(accepted, products)
# print(type(products_sample)) # <class 'filter'>
# print(*products_sample) # iPad iPhone iRiver


'''
+ lambda -функции
'''
# numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]
#
# positive_numbers = list(filter(lambda el: el > 0, numbers))
# large_numbers = list(filter(lambda x: x > 50, numbers))
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#
# print(positive_numbers)
# print(large_numbers)
# print(even_numbers)




# products = ['Samsung Galaxy', 'iPad', 'iPhone', 'iRiver']
#
# def find_len(el):
#     return len(el) > 4
#
#
# new_words1 = [p for p in products if len(p) > 4]
# new_words1 = filter(lambda p: len(p) > 4, products)
# new_words2 = list(filter(lambda p: 'e' in p, products))
#
#
# new_words1 = [p for p in products if len(p) > 6] # [что откуда условие]
# new_dict = {i: p for i, p in enumerate(products) if len(p) > 4}
#
# print(new_dict)
#
# new_words3 = []
# for p in products:
#     if len(p) > 6:
#         new_words3.append(p)
#
#
# print(*new_words1)
# print(new_words2)
# print(new_words3)

# a = 3
# b = 5
# a, b = b, a
# print(a, b)
'''
ЗАДАЧА
Вывести товары, которые начинаются на i'''
# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'IRiver']
#
# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'IRiver']
# print(*(filter(lambda x: x.lower().startswith('i'), products)))












# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'IRiver']

# def sort_f(x):
#     return x.lower().startswith('ipa')

# products_sample = filter(lambda x: 'a' in x.lower(), products)
# print(*products_sample)


'''
map(func, *iterables)
func - функция, которой будет передаваться текущий элемент последовательности.
Внутри функции func необходимо вернуть новое значение.
*iterables - последовательности:  списки, строки, кортежи, множества, словари.
'''

#
# def mult(num):
#     return num * 5


# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = map(mult, numbers)
# print(new_numbers)
# #
# print(*new_numbers)
# new_numbers = map(mult, numbers)
# print(list(new_numbers))

# def func(elem1, elem2, elem3):
#     return elem1 + elem2 + elem3
#
#
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [10, 20, 30, 40, 50]
# numbers3 = [100, 200, 300, 400, 500]
#
# new_numbers = list(map(func, numbers1, numbers2, numbers3))
#
# print(new_numbers)

'''
ЗАДАЧА. Есть список с ценами на товары (тип данных — str ), получить из него
кортеж с ценами (тип данных — float )
'''
# prices = ['1578.4', '892.4', '354.1', '871.5']
#
# prices_tup = tuple(map(float, prices))
#
# print(prices_tup)
#
# #
# prices_float = tuple(map(float, prices))
# print(type(prices[0]), type(prices_float[0]), prices_float)


'''
+lambda
'''
# numbers = [1, 2, 3, 4, 5, 6]
#
# new_numbers1 = list(map(lambda x: x+1, numbers))
# new_numbers2 = list(map(lambda x: x*2, numbers))
# new_numbers3 = list(map(lambda x: x**2, numbers))
#
# print(new_numbers1)
# print(new_numbers2)
# print(new_numbers3)


# strings = ['a', 'b', 'c', 'd', 'e']
# numbers = [3, 2, 1, 4, 5]
#
# new_strings = list(map(lambda x, y: x*y, strings, numbers))
#
# print(new_strings)



'''
ЗАДАЧА
применить скидку к товарам и округлить до 2 знака
'''
# DISCOUNT = 7
# prices = ['1578.4', '892.4', '354.1', '871.5']

# prices = list(map(float, prices))
# new_prices = list(map(lambda x: x * 0.93, prices))
# print(new_prices)
# d = 7
# prices = ['1578.4', '892.4', '354.1', '871.5']
#
# print(list(map(lambda x: round(float(x) * (1-d/100), 2), prices)))











#
# prices_discount = map(
#     lambda x: round(float(x) * (100 - DISCOUNT) / 100, 2),
#     prices
# )
# print(*prices_discount)

'''
А если данные с ошибками?
+ filter
+ lambda
'''
# prices = ['15,78.4', '892.4', '354.1 rub', '871.5', '47,1']
# prices_float = map(float, filter(lambda x: x.replace('.', '', 1).isdigit(), prices)) # Для метода .replace() задали количество замен 1, чтобы из настоящих вещественных получились только цифры — их фильтр пропустит.
# print(*prices_float)


'''
zip() объединяет отдельные элементы из каждой переданной ей последовательности (итерируемого объекта) в кортежи.
'''

# numbers = [1, 2, 3]
# words = ['one', 'two', 'three']
#
# result = zip(numbers, words)
#
# print(result)
# print(list(result))


# numbers = [1, 2, 3]
# words = ['one', 'two', 'three']
# russian = ['один', 'два', 'три']
#
# result = zip(numbers, words, russian)
# print(list(result))


'''Для создания словарей'''

# keys = ['name', 'age', 'gender']
# values = ['Bob', 23, 'male']
#
# info = dict(zip(keys, values))
# print(info)


'''
ЗАДАЧА
Пусть есть три списка: имена пользователей, их логины и роли. Нужно вывести информацию о
каждом пользователе. '''
# user_names = ['Иван', 'Петр', ]
# user_logins = ['ivan', 'petr', 'olga', 'sergey']
# user_roles = ['user', 'staff', 'admin', 'user']



# from itertools import zip_longest
#
# new_list = list(zip_longest(user_names, user_logins, user_roles))
# print(new_list)

# result = list(zip(user_names, user_logins, user_roles))
# print(result)


#
# for name, login, role in zip(user_names, user_logins, user_roles):
#     print(f' {name} , {login} , {role} ')

'''
enumerate() возвращает кортеж из индекса элемента и самого элемента переданной ей последовательности (итерируемого объекта).
'''

# colors = ['red', 'green', 'blue']
#
# for pair in enumerate(colors):
#     print(pair)


'''
Если счет нужно начать с отличного от нуля числа, то нужно передать значение аргумента start.
'''
#
# colors = ['red', 'green', 'blue']
# ind = 5
# for k, v in enumerate(colors, ind+1):
#     print({k: v})
#
#
# colors = ['red', 'green', 'blue']
#
# pairs = enumerate(colors)
#
# print(pairs)
# print(list(pairs))


# colors = ['red', 'green', 'blue']
# for index, item in enumerate(colors):
#     print(index, item)
# #
# # '''Такой код является альтернативой коду:'''
# #
# colors = ['red', 'green', 'blue']
# for i in range(len(colors)):
#     print(i, colors[i])
