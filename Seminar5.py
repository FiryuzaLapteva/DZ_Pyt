# 42. Есть список чисел. Вывести – является ли последовательность строго убывающей, 
# или строго возрастающей, или ни то, ни другое
# def check_sorted(somelist):
#     if sorted(set(somelist)) == somelist:
#         return 1
#     elif sorted(set(somelist), reverse=True) == somelist:
#         return -1
#     return 0
# s_dict = {
#     1: 'Возрастает',
#     -1: 'Убывает',
#     0: 'Ни то, ни то'
#           }

# print(s_dict[check_sorted([1, 2, 3])])
# print(s_dict[check_sorted([3, 2, 3])])
# print(s_dict[check_sorted([3, 2, 1])])
# print(check_sorted([1, 1, 2, 3]))

# from operator import sub

# my_list = [6, 5, 4, 3, 2, 1]
# list2 = my_list.copy()# Создаем копию списка my_list
# del list2[0] #Удаляем элеменет под индексом [0]

# sub_iter = list(map(sub, list2, my_list)) #Вычитаем итерационно список list2 из my_list
# print (list(sub_iter))

# if sub_iter[0] == 1 and len(sub_iter) == sub_iter.count(sub_iter[0]):
#     print('Возрастающая')
# if sub_iter[0] == -1 and len(sub_iter) == sub_iter.count(sub_iter[0]):
#     print('Убывающая')
# else:
#     print('Ни то, ни то')

# 43. Дана последовательность чисел. Получить отсортированный по возрастанию список 
# уникальных элементов заданной последовательности.
# 	Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]




# 44. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# 	Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;




# matrix = [[1, 3, 2], [9, 9, 8], [4, 5, 6]]
# matrix1 = [item for j in matrix for item in j]
# print(sorted(matrix1) != [1,2,3,4,5,6,7,8,9])
# def any_duplicates(matr):
#     perfect_array = [1,2,3,4,5,6,7,8,9]
#     array = []
#     for i in matr:
#         for j in i:
#             array.append(j)
#     sorted_array = sorted(array)
#     return sorted_array != perfect_array
# print(any_duplicates(matrix))

# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# 	Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# **Добавьте возможность использования скобок, меняющих приоритет операций.
# 	Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;
