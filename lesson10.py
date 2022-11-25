import requests

# делаем запрос по адресу
# response = requests.get('https://geekbrains.ru/')
# print(response) # 200 - ответ по запросу, говорит о том, что запрос прошел успешно.
# print('*' * 50)
# print(dir(response))
# print('*' * 50)
# print(type(response))
#
# print(response.status_code)
# #
# if response:
#     print('Ok')
#
# if response.status_code == 200:
#     print('Ok')


'''
атрибут headers — словарь с заголовками ответа сервера;
атрибут status_code — число, код ответа сервера;
атрибут content — содержимое ответа в байтах;
метод close() — освобождает (закрывает) соединение.
'''

'''
Response.apparent_encoding возвращает кодировку, угаданную chardet,
Response.close() освобождает соединение с пулом,
Response.cookies возвращает cookies, установленные сервером,
Response.elapsed возвращает время, потраченное на запрос,
Response.encoding устанавливает кодировку, для декодирования,
Response.history возвращает историю перенаправлений,
Response.is_permanent_redirect определение постоянных редиректов,
Response.is_redirect есть ли редирект,
Response.iter_content() перебирает данные ответа кусками,
Response.iter_lines() перебирает данные ответа, по одной строке,
Response.json() возвращает ответ в виде JSON,
Response.links возвращает ссылки заголовка ответа,
Response.next возвращает объект PreparedRequest,
Response.ok True, если status_code меньше 400,
Response.raise_for_status() вызывает исключение HTTPError,
Response.raw возвращает ответа в виде файлового объекта,
Response.reason возвращает текстовое представление ответа,
Response.request возвращает объект PreparedRequest запроса,
Response.status_code возвращает код ответа сервера,
Response.text возвращает контент ответа сервера в юникоде,
Response.url возвращает URL-адрес, после перенаправлений.
'''

# print(response.content)

# response.encoding = 'utf-8'
# print(response.text)


# from requests import get, utils
# encodings = utils.get_encoding_from_headers(response.headers)
# content = response.content.decode(encoding=encodings)
# print(content)

# text = response.text
# print(text)


# response = requests.get('https://api.github.com/')
# data = response.text
# print(data)
# print(type(response.text))


# data = response.json()
# print(data)
# print(type(data))

from pprint import pprint
# data = response.json()
# pprint(data, indent=10, sort_dicts=True)



# git_response = response.headers
# print(git_response)
# print(git_response['server'])


# Передаем параметры
# jph_data = requests.get('https://jsonplaceholder.typicode.com/comments', params=b'postId=2')
# pprint(jph_data.json())






# import requests
from decimal import *
from datetime import datetime
#
# getcontext().prec = 4
# response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
# pprint(response)
#
# def currency_rates(val):
#     val = val.upper()
#     response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
#
#     if val not in response:
#         return None
#
#     rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
#     day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
#     day, month, year = map(int, day_raw)
#     return f"{Decimal(rub.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"
#
#
# print(currency_rates('USD'))
# print(currency_rates('EUR'))
# print(currency_rates('eur'))

#
# import requests
# from pprint import pprint
# data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# pprint(data)
# cur = input()
# print(data['Valute'][cur]['Name'], data['Valute'][cur]['Value'], data['Date'])

