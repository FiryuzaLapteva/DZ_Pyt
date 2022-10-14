# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на введенных пользователем позициях.

number = int(input ('Введите целое число  '))
my_list = []
for i in range(- number,number +1):
    my_list.append(i)
print(my_list)

pos1 = int(input('Введите первую позицию элемента ' ))
print(my_list[pos1 -1])
pos2 = int(input('Введите вторую позицию элемента ' ))
print(my_list[pos2 -1])
print(f'Произведение элементов = {(my_list[pos1 -1])*(my_list[pos2 -1])}')


        
   
