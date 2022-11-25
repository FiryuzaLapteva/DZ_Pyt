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
                            text=f'Привет, {update.effective_user.first_name}'
                            'Введите сокращенное обозначение валюты')              
# обработчик функции start_command 
start_command = CommandHandler('start', start_command)
dispatcher.add_handler(start_command)

def process_coin_step (update: Update, context: CallbackContext):
    response = requests.get(config.url).json()
    for coin in response:
            if (update.message.text == coin ['CharCode']):
                context.bot.send_message (chat_id=update.effective_chat.id,
                                            printCoin(coin ['Nominal'], coin ['Name'],
                                            coin['Value']))    

pr_coin_step = MessageHandler(Filters.text & (~Filters.command), process_coin_step)
dispatcher.add_handler(pr_coin_step)

def printCoin(Nominal, Name, Value):
    '''Вывод курса пользователю'''
    return str (Nominal) + str (Name)+ '=' + str(Value) + ' рублей'

# def echo(update: Update, context: CallbackContext):
#     logger_bd(update, context)
#     msg = update.message.text 
#     context.bot.send_message(chat_id=update.effective_chat.id, text= msg)

# # обработчик текстовых сообщений
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)# функция обработки текстовых сообщений


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