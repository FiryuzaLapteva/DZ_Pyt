import config
import telebot
import requests
from telebot import types

bot = telebot.TeleBot(config.token)
response = requests.get(config.url).json()
@bot.message_handler(commands=['start', 'help'])

def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('USD')
    itembtn2 = types.KeyboardButton('EUR')
    itembtn3 = types.KeyboardButton('RUB')
    markup.add(itembtn1, itembtn2, itembtn3)# список кнопок
    msg = bot.send_message(message.chat.id, 'Узнать наличный курс', reply_markup=markup)
    




if __name__ == '__main__':
    op