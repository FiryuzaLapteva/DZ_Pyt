from telegram.ext import Updater
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import MessageHandler, Filters
import logging
import config
import requests
from logger import logger_bd

# Создаем объект updater куда помещаем токен бота
updater = Updater(token=config.token)
response = requests.get(config.url).json() #декодирует данные с url адреса json
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
    "\n  Введи /many <символьное обозначение валюты, например USD>, если хочешь узнать курс валюты")
updater.dispatcher.add_handler(CommandHandler('menu', menu_command))

def process_coin_step (CharCode):
    response = requests.get(config.url).json()
    return response['Valute'][CharCode]['Name'], response['Valute'][CharCode]['Value'], response['Date']

def many_command(update: Update, context: CallbackContext):
    msg = update.message.text
    logger_bd(update, context)
    items = msg.upper().split() 
    print(msg)
    items = items[1]
    context.bot.send_message (chat_id=update.effective_chat.id,
                            text=f'{process_coin_step(items)}')
updater.dispatcher.add_handler(CommandHandler('many', many_command))

#



# обработка команды старт (создаем Inline клавиатуру)
# def startCommand(update: Update, context: CallbackContext):
#     buttonA = telegram.InlineKeyboardButton('Поздороваться', callback_data='buttonA')
#     buttonB = telegram.InlineKeyboardButton('Посчитать сумму', callback_data='buttonB')
#     buttonC = telegram.InlineKeyboardButton('Поменять список', callback_data='buttonC')
#     buttonD = telegram.InlineKeyboardButton('Прогноз погоды', callback_data='buttonD')
#     markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD]])
#     start_command_handler = CommandHandler('start', startCommand)
#     CallbackQueryHandler(callback=callback, pattern=None, run_async=False)


#     update.message.reply_text('Добрый день! Чтобы начать работу, выберите одно из возможных действий',
#                               reply_markup=markup)
#     return callback


# # обработка нажатия клавиш клавиатуры
# def callback(update: Update, context: CallbackContext):
#     query = update.callback_query
#     variant = query.data
#     if variant == 'buttonA':
#         query.answer()
#         query.edit_message_text(text='Хотите поздороваться? Скажите привет!')

#     if variant == 'buttonB':
#         query.answer()
#         query.edit_message_text(text='Введите "Сумма: 2 числа через пробел"')

#     if variant == 'buttonC':
#         query.answer()
#         query.edit_message_text(text='Введите "Список: список через запятую"')

#     if variant == 'buttonD':
#         query.answer()
#         query.edit_message_text(text='Напишите: "Город: свой город"')
# # def echo(update: Update, context: CallbackContext):
# #     logger_bd(update, context)
# #     msg = update.message.text 
# #     context.bot.send_message(chat_id=update.effective_chat.id, text= msg)

# # # обработчик текстовых сообщений
# # echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# # dispatcher.add_handler(echo_handler)# функция обработки текстовых сообщений


# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Sorry, I didn't understand that command.")   

# обработчик не распознанных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск бота
updater.start_polling()
# обработчик нажатия Ctrl+C
updater.idle()