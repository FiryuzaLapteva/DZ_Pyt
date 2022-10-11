# colors = ['red', 'green', 'white']

# print(type(colors))
# print(dir(colors))



'''
Метод append() принимает единственный аргумент:
item – элемент, который нужно добавить в конец списка. Элементом могут быть числа, строки, словари, другой список и т.д.
'''
# colors = ['red', 'green', 'white']
# print(colors)
# colors.append('black')
# print(colors)


'''
Метод insert() позволяет вставлять значение в список в заданной позиции. В него передается два аргумента:
index: индекс, задающий место вставки значения;
value: значение, которое требуется вставить.
'''
# colors = ['red', 'green', 'white']
# print(colors)
# colors.insert(0, 'black')
# print(colors)
# colors.insert(3, 'yellow')
# print(colors)

'''
Метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению. 
Таким образом, в метод передается один параметр:
value: значение, индекс которого требуется найти.
Если элемент в списке не найден, то во время выполнения происходит ошибка.
'''

# colors = ['red', 'green', 'white']
# position = colors.index('green')
# print(position)
#
# position = colors.index('violet')
# print(position)
#
# if 'violet' in colors:
#     position = colors.index('violet')
#     print(position)
# else:
#     print('Такого значения нет в списке')

'''
Метод remove() удаляет первый элемент, значение которого равняется переданному в метод значению. 
В метод передается один параметр:
value: значение, которое требуется удалить.
Метод уменьшает размер списка на один элемент. Все элементы после удаленного элемента смещаются на одну позицию к началу списка. 
Если элемент в списке не найден, то во время выполнения происходит ошибка.

Важно: метод remove() удаляет только первый элемент с указанным значением. Все последующие его вхождения остаются в списке. 
Чтобы удалить все вхождения нужно использовать цикл while в связке с оператором принадлежности in и методом remove.
'''
# colors = ['red', 'green', 'white', 'yellow', 'white']
# colors.remove('white')
# print(colors)

'''
Метод pop() удаляет элемент по указанному индексу и возвращает его. В метод pop() передается один необязательный аргумент:
index: индекс элемента, который требуется удалить.
Если индекс не указан, то метод удаляет и возвращает последний элемент списка. 
Если список пуст или указан индекс за пределами диапазона, то во время выполнения происходит ошибка.
'''

# colors = ['red', 'green', 'white', 'yellow']
# item = colors.pop()
# print(item)
# print(colors)

'''
Метод count() возвращает количество элементов в списке, значения которых равны переданному в метод значению. 

В метод передается один параметр:
value: значение, количество элементов, равных которому,  нужно посчитать.
Если значение в списке не найдено, то метод возвращает 0.
'''

# colors = ['red', 'green', 'white', 'yellow', 'green', 'blue', 'green']
# cnt1 = colors.count('red')
# cnt2 = colors.count('violet')
# cnt3 = colors.count('green')
#
# print(cnt1)
# print(cnt2)
# print(cnt3)

'''
Метод reverse() инвертирует порядок следования значений в списке, то есть меняет его на противоположный. in place
Существует большая разница между вызовом метода names.reverse() и использованием среза [::-1]. 
Метод reverse() меняет порядок элементов на обратный в текущем списке, 
а срез создает копию списка, в котором элементы следуют в обратном порядке.
'''

# colors = ['red', 'green', 'white', 'yellow']
# print(id(colors), colors) # id() возвращает уникальный id для указанного объекта (адрес памяти объекта) - отличается при каждом запуске программы.
# colors.reverse()
# print(id(colors), colors)
#
#
# colors = ['red', 'green', 'white', 'yellow']
# print(id(colors), colors)
# colors_reversed = list(reversed(colors))
# print(id(colors_reversed), colors_reversed)
# print(id(colors[::-1]), colors[::-1])


'''
Метод sort() меняет состояние списка и расставляет элементы по возрастанию. in place
'''

# colors = ['red', 'green', 'white', 'yellow']
# print(id(colors), colors)
# colors.sort()
# print(id(colors), colors)


# colors = ['red', 'green', 'white', 'yellow']
# print(id(colors), colors)
# colors_sorted = list(sorted(colors))
# print(id(colors_sorted), colors_sorted)

'''
Метод clear() удаляет все элементы из списка.
'''

# colors = ['red', 'green', 'white', 'yellow']
# colors.clear()
# print(colors)


'''
Индексация и срезы
'''

# year_months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
# first_quarter = year_months[0:3]
# print(first_quarter)
# other_first_quarter = year_months[: 3]
# print(other_first_quarter)

#range(start, stop, step)
# list[start: stop: step]

# second_half_year = year_months[6:]  # second_half_year = year_months[6: 1000]
# print(second_half_year)


# odd_months = year_months[:: 2]
# print(odd_months)


# even_months = year_months[1:: 2]
# print(even_months)
#
# even_months = year_months[-1]
# print(even_months)

# my_str = 'Какая-то строка'
# print(my_str[1::3])

'''
Метод copy() создает поверхностную копию списка.
'''

# colors = ['red', 'green', 'white', 'yellow']
# colors_copy = colors.copy()
#
# print(colors)
# print(colors_copy)
