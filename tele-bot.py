import re
import telegram
import json
import requests as req
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler

updater = Updater('5747203558:AAFta3KOWVkQtBSkJw5HDqMbuSoF0Y99E_E', use_context=True)
dispatcher = updater.dispatcher


# обработка команды старт (создаем Inline клавиатуру)
def startCommand(update: Update, context: CallbackContext):
    buttonA = telegram.InlineKeyboardButton('Поздороваться', callback_data='buttonA')
    buttonB = telegram.InlineKeyboardButton('Посчитать сумму', callback_data='buttonB')
    buttonC = telegram.InlineKeyboardButton('Поменять список', callback_data='buttonC')
    buttonD = telegram.InlineKeyboardButton('Прогноз погоды', callback_data='buttonD')
    markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD]])

    update.message.reply_text('Добрый день! Чтобы начать работу, выберите одно из возможных действий',
                              reply_markup=markup)
    return callback


# обработка нажатия клавиш клавиатуры
def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonA':
        query.answer()
        query.edit_message_text(text='Хотите поздороваться? Скажите привет!')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Введите "Сумма: 2 числа через пробел"')

    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Введите "Список: список через запятую"')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_text(text='Напишите: "Город: свой город"')


from geopy import geocoders
from yaweather import Russia, YaWeather


# функция получения погоды
def get_weather(city: str):
    geolocator = geocoders.Nominatim(user_agent="telebot")
    latitude = geolocator.geocode(city).latitude
    longitude = geolocator.geocode(city).longitude
    url_yandex = f'https://api.weather.yandex.ru/v2/informers/?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = req.get(url_yandex, headers={'X-Yandex-API-Key': 'ee2fec66-a36e-453e-8f3b-21bbbb2e5cb2'}, verify=False)
    conditions = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
                  'overcast': 'пасмурно', 'drizzle': 'морось', 'light-rain': 'небольшой дождь',
                  'rain': 'дождь', 'moderate-rain': 'умеренно сильный', 'heavy-rain': 'сильный дождь',
                  'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
                  'wet-snow': 'дождь со снегом', 'light-snow': 'небольшой снег', 'snow': 'снег',
                  'snow-showers': 'снегопад', 'hail': 'град', 'thunderstorm': 'гроза',
                  'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'
                  }
    wind_dir = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное', 'e': 'восточное',
                'se': 'юго-восточное', 's': 'южное', 'sw': 'юго-западное', 'w': 'западное', 'с': 'штиль'}
    print(yandex_req.text)

    yandex_json = json.loads(yandex_req.text)
    yandex_json['fact']['condition'] = conditions[yandex_json['fact']['condition']]
    yandex_json['fact']['wind_dir'] = wind_dir[yandex_json['fact']['wind_dir']]
    for parts in yandex_json['forecast']['parts']:
        parts['condition'] = conditions[parts['condition']]
        parts['wind_dir'] = wind_dir[parts['wind_dir']]

    pogoda = dict()
    params = ['condition', 'wind_dir', 'pressure_mm', 'humidity']
    for parts in yandex_json['forecast']['parts']:
        pogoda[parts['part_name']] = dict()
        pogoda[parts['part_name']]['temp'] = parts['temp_avg']
        for param in params:
            pogoda[parts['part_name']][param] = parts[param]

    pogoda['fact'] = dict()
    pogoda['fact']['temp'] = yandex_json['fact']['temp']
    for param in params:
        pogoda['fact'][param] = yandex_json['fact'][param]

    pogoda['link'] = yandex_json['info']['url']
    return pogoda

    # # y = YaWeather(api_key='ee2fec66-a36e-453e-8f3b-21bbbb2e5cb2')
    # # res = y.forecast(Russia.city)
    # forecast = f'cейчас {res.fact.temp} °C, oщущается как {res.fact.feels_like} °C'
    # return forecast


# печать прогноза погоды
def print_weather(update: Update, context: CallbackContext):
    city = update.message.text
    print(city.split()[1])
    forecast = get_weather(re.sub('Город: ', '', city))
    print(forecast)
    update.message.reply_text(f'Погода в городе {city[7:]}: {forecast}', parse_mode='Markdown')


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


# def startCommand(update: Update, context: CallbackContext):
#     update.message.reply_text('Привет! Я могу поболтать')

def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


# bad_list = инженер-конструктор Игорь, главный бухгалтер МАРИНА, токарь высшего разряда нИКОЛАй, директор аэлита
def change_list(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split(', ')
    items[0] = items[0].replace('Список: ', '')
    print(items)
    update.message.reply_text(', '.join(el.title() for el in items))


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
hello_handler = MessageHandler(Filters.regex('Привет'), hello)
sum_handler = MessageHandler(Filters.regex('Сумма: '), sum_command)
list_handler = MessageHandler(Filters.regex('Список: '), change_list)
weather_handler = MessageHandler(Filters.regex('Город: '), print_weather)
callback_button_handler = CallbackQueryHandler(callback=callback, pattern=None, run_async=False)

# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(callback_button_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(weather_handler)
dispatcher.add_handler(list_handler)
dispatcher.add_handler(sum_handler)

# Начинаем поиск обновлений
updater.start_polling()
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()

# updater.dispatcher.add_handler(CommandHandler("start", startCommand))
# updater.dispatcher.add_handler(CommandHandler('hello', hello))
# updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
# updater.dispatcher.add_handler(CommandHandler('empl', change_list))
#
# updater.start_polling()
# updater.idle()
