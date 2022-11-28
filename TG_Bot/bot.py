from telegram.ext import Updater
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import logging
import config
import requests
from logger import logger_bd

# Создаем объект updater куда помещаем токен бота
updater = Updater(token=config.token)
# Создаем диспетчер
dispatcher = updater.dispatcher
# Функция логирования для отслеживания ошибок
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


# обработка команды старт (создаем Inline клавиатуру)
def start(update: Update, context: CallbackContext):
    logger_bd(update, context)
    buttonA = InlineKeyboardButton('Menu', callback_data='buttonA')
    buttonB = InlineKeyboardButton('Money', callback_data='buttonB')
    buttonC = InlineKeyboardButton('Calc_r', callback_data='buttonC')
    buttonD = InlineKeyboardButton('Calc_c', callback_data='buttonD')
    markup = InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD]])
    updater.dispatcher.add_handler(CallbackQueryHandler(callback=callback1, pattern=None, run_async=False)
)
    update.message.reply_text('Добрый день! Чтобы начать работу, выберите одно из' 
                                ' возможных действий', reply_markup=markup)
    return callback1
updater.dispatcher.add_handler(CommandHandler('start', start))

#  обработка нажатия клавиш клавиатуры старт
def callback1(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonA':
        query.answer()
        query.edit_message_text(text='Введите /menu')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Введите /money <сокращенное обозначение валюты>, например /Money USD')

    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Введите /Calc_r <пример> через пробел, например, /Calc_r 2 + 2 или /Calc_r 4 - 2 ')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_text(text='Введите /Calc_c <пример> через пробел, например, /Calc_c (2+2j) - (3-2j) или /Calc_c (4-2j) * (2+2j) ')

def menu_command(update: Update, context: CallbackContext):
    logger_bd(update, context)
    update.message.reply_text(f" {update.effective_user.first_name}!"\
    "\n  Введи /menu, если хочешь посмотреть меня"
    "\n  Введи /money <символьное обозначение валюты, например USD>, если хочешь узнать курс валюты"
    "\n /calc_r, здесь вы можете произвести математические операции с рациональными числами"
    "\n /calc_c, здесь вы можете произвести математические операции с комплексными числами")
updater.dispatcher.add_handler(CommandHandler('menu', menu_command))

def process_coin_step (CharCode):
    response = requests.get(config.url).json()
    return response['Valute'][CharCode]['Name'], response['Valute'][CharCode]['Value'], response['Date']

def money_command(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    items = msg.upper().split() 
    print(msg)
    items = items[1]
    context.bot.send_message (chat_id=update.effective_chat.id,
                            text=f'{process_coin_step(items)}')
updater.dispatcher.add_handler(CommandHandler('money', money_command))

def Calc_r(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    print(msg)
    items = msg.split()  # /2 + 2
    x = float(items[1])
    z = items[2]
    y = float(items[3])
    if z == "+":
        update.message.reply_text(f'{x} {z} {y} = {x + y}')
    elif z == "-":
        update.message.reply_text(f'{x} {z} {y} = {x - y}')
    elif z == "*":
        update.message.reply_text(f'{x} {z} {y} = {x * y}')
    elif z == "/":
        update.message.reply_text(f'{x} {z} {y} = {x / y}')

updater.dispatcher.add_handler(CommandHandler('Calc_r', Calc_r))

def Calc_c(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    print(msg)
    items = msg.split()  # /2 + 2
    x = complex(items[1])
    z = items[2]
    y = complex(items[3])
    if z == "+":
        update.message.reply_text(f'{x} {z} {y} = {x + y}')
    elif z == "-":
        update.message.reply_text(f'{x} {z} {y} = {x - y}')
    elif z == "*":
        update.message.reply_text(f'{x} {z} {y} = {x * y}')
    elif z == "/":
        update.message.reply_text(f'{x} {z} {y} = {x / y}')

updater.dispatcher.add_handler(CommandHandler('Calc_c', Calc_c))

# функция обработки не распознанных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Извините, я не знаю такой команды")   

# обработчик не распознанных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск бота
updater.start_polling()
# обработчик нажатия Ctrl+C
updater.idle()