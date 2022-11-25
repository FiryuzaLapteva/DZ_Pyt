from telegram.ext import Updater
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import MessageHandler, Filters


def logger_bd(update: Update, context: CallbackContext):
    file = open('db.csv', 'a', encoding= 'utf -8')
    file.write(f'{update.effective_user.first_name}, {update.effective_chat.id}, {update.message.text}\n')
    file.close