import csv


def append_user(dict1):
    with open('DATABASE.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        max_id = 1
        for row in reader:
            print(row)
            print(row['id'], type(row['id']))
            if max_id < int(row['id']):
                max_id = int(row['id'])
    print(max_id)

    dict1['id'] = str(max_id + 1)
    with open('DATABASE.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writerow(dict1)



