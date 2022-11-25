from telegram.ext import Updater
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import MessageHandler, Filters
from bot import dispatcher
import datetime




# функция обработки команды '/start
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                            text="I'm a bot, please talk to me!")                    
# обработчик функции /start 
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# функция обработки команды time_command
def time_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                            text=f'{datetime.datetime.now()}')                    
# обработчик функции time_command 
time_handler = CommandHandler('time', time_command)
dispatcher.add_handler(time_handler)

# функция обработки команды help_command
def help_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                            text=f'/start\n/time\n/help')                    
# обработчик функции help_command 
help_handler = CommandHandler('help', help_command)
dispatcher.add_handler(help_handler)

# функция обработки команды sum_command
# def sum_command(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.effective_chat.id, 
#                             text="I'm a bot, please talk to me!")                    
# # обработчик функции sum_command 
# start_handler = CommandHandler('sum', sum_command)
# dispatcher.add_handler(start_handler)