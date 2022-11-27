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


# функция обработки команды start_command
def start_command(update: Update, context: CallbackContext):
    logger_bd(update, context)
    context.bot.send_message (chat_id=update.effective_chat.id,
                            text=f'Привет, {update.effective_user.first_name},'
                            ' я телеграм - бот. Введи /menu, чтобы ознакомиться с моими возможностями')              
# обработчик функции start_command 
start_command = CommandHandler('start', start_command)
dispatcher.add_handler(start_command)

def menu_command(update: Update, context: CallbackContext):
    logger_bd(update, context)
    update.message.reply_text(f" {update.effective_user.first_name}!"\
    "\n  Введи /menu, если хочешь посмотреть меня"
    "\n  Введи /money <символьное обозначение валюты, например USD>, если хочешь узнать курс валюты"
    "\n Введи /calc_r, если хотите произвести операции с рациональными числами"
    "\n Введи /calc_c, если хотите произвести операции с комплексными числами")
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

def Summa(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    print(msg)
    items = msg.split()  # /2 + 2
    x = float(items[1])
    z = items[2]
    y = float(items[3])
    update.message.reply_text(f'{x} {z} {y} = {x + y}')
updater.dispatcher.add_handler(CommandHandler('Summa', Summa))

def Sub(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    print(msg)
    items = msg.split()  # /2 - 2
    x = float(items[1])
    z = items[2]
    y = float(items[3])
    update.message.reply_text(f'{x} {z} {y} = {x - y}')
updater.dispatcher.add_handler(CommandHandler('Sub', Sub))

def Multi(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    print(msg)
    items = msg.split()  # /2 - 2
    x = float(items[1])
    z = items[2]
    y = float(items[3])
    update.message.reply_text(f'{x} {z} {y} = {x * y}')
updater.dispatcher.add_handler(CommandHandler('Multi', Multi))

def Div(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    print(msg)
    items = msg.split()  # /2 - 2
    x = float(items[1])
    z = items[2]
    y = float(items[3])
    update.message.reply_text(f'{x} {z} {y} = {x / y}')
updater.dispatcher.add_handler(CommandHandler('Div', Div))



# обработка команды калькулятор - рациональные числа (создаем Inline клавиатуру)
def calc_r(update: Update, context: CallbackContext):
    logger_bd(update, context)
    buttonA = InlineKeyboardButton('Summa', callback_data='buttonA')
    buttonB = InlineKeyboardButton('Sub', callback_data='buttonB')
    buttonC = InlineKeyboardButton('Multi', callback_data='buttonC')
    buttonD = InlineKeyboardButton('Div', callback_data='buttonD')
    markup = InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD]])
    updater.dispatcher.add_handler(CallbackQueryHandler(callback=callback1, pattern=None, run_async=False)
)
    update.message.reply_text('Добрый день! Чтобы начать работу, выберите одно из' 
                                ' возможных действий', reply_markup=markup)
    return callback1
updater.dispatcher.add_handler(CommandHandler('calc_r', calc_r))

#  обработка нажатия клавиш клавиатуры
def callback1(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonA':
        query.answer()
        query.edit_message_text(text='Введите "/Summa 2 + 2"')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Введите" /Sub 4 - 2 "')

    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Введите" /Multi  4 - 2 "')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_text(text='Введите" /Div  4 - 2 "')

def SummaС(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    items = msg.split()
    x = complex(items[1])
    z = items[2]
    y = complex(items[3])

    update.message.reply_text(f'{x} {z} {y} = {x + y}')
updater.dispatcher.add_handler(CommandHandler('SummaC', SummaС))

def SubC(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    print(msg)
    items = msg.split()
    x = complex(items[1])
    z = items[2]
    y = complex(items[3])
    update.message.reply_text(f'{x} {z} {y} = {x - y}')
updater.dispatcher.add_handler(CommandHandler('SubC', SubC))

def MultiC(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    print(msg)
    items = msg.split()
    x = complex(items[1])
    z = items[2]
    y = complex(items[3])
    update.message.reply_text(f'{x} {z} {y} = {x * y}')
updater.dispatcher.add_handler(CommandHandler('MultiC', MultiC))

def DivC(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    print(msg)
    items = msg.split()
    x = complex(items[1])
    z = items[2]
    y = complex(items[3])
    update.message.reply_text(f'{x} {z} {y} = {x / y}')
updater.dispatcher.add_handler(CommandHandler('DivC', DivC))

# обработка команды калькулятор - комплекные числа (создаем Inline клавиатуру)
def calc_c(update: Update, context: CallbackContext):
    logger_bd(update, context)
    buttonE = InlineKeyboardButton('SummaС', callback_data='buttonE')
    buttonF = InlineKeyboardButton('SubС', callback_data='buttonF')
    buttonG = InlineKeyboardButton('MultiС', callback_data='buttonG')
    buttonS = InlineKeyboardButton('DivС', callback_data='buttonS')
    markup = InlineKeyboardMarkup(inline_keyboard=[[buttonE], [buttonF], [buttonG], [buttonS]])
    updater.dispatcher.add_handler(CallbackQueryHandler(callback=callback2, pattern=None, run_async=False)
)
    update.message.reply_text('Добрый день! Чтобы начать работу, выберите одно из' 
                                ' возможных действий', reply_markup=markup)
    return callback2
updater.dispatcher.add_handler(CommandHandler('calc_c', calc_c))

#  обработка нажатия клавиш клавиатуры
def callback2(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonE':
        query.answer()
        query.edit_message_text(text='Введите /SummaC (1+2j) + (1+2j)')

    if variant == 'buttonF':
        query.answer()
        query.edit_message_text(text='Введите  /SubC (1+2j) - (1+2j)')

    if variant == 'buttonG':
        query.answer()
        query.edit_message_text(text='Введите /MultiC (1+2j) * (1+2j)')

    if variant == 'buttonS':
        query.answer()
        query.edit_message_text(text='Введите /DivC (1+2j) / (1+2j)')

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