import csv

with open('csv_example_1.csv', 'w', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    
    csv_writer.writerow(['Цвет', 'Размер', 'Количество', 'Ответственный'])
    csv_writer.writerow(['Красный', '15', '7'])
    csv_writer.writerow([i for i in range(1, 6)])


with open('csv_example_2.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'first_name', 'second_name', 'last_name']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    csv_writer.writeheader()
    for i in range(1, 11):
        csv_writer.writerow(
            {'id': i, 'second_name': f"отчество_{i}",
            'first_name': f"имя_{i}", 'last_name': f"фамилия_{i}"}
        )
        # чтобы запись была без пустых строчек
with open('csv_example_2.csv', 'w', encoding='utf-8', newline='') as csvfile:

def gert_value_mod_3():
    fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
    dict_data = ()
    for el in fieldnames:
        dict_data[el] = input(f'Введите {el}')
    return dict_data








        # csv_writer.writerow({'id': 11, 'second_name': "Иванович",
        #                  'first_name': "Иван",
        #                  'last_name': "Иванов"})
        #


    
