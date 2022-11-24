import config
import telebot
import requests
from telebot import types

bot = telebot.TeleBot(config.token)
response = requests.get(config.url).json() #декодирует json
@bot.message_handler(commands=['start', 'help'])


def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    #resize_keyboard - маленькая клавиатура
    itembtn1 = types.KeyboardButton('USD')
    itembtn2 = types.KeyboardButton('EUR')
    itembtn3 = types.KeyboardButton('KZT')
    markup.add(itembtn1, itembtn2, itembtn3)# список кнопок
    msg = bot.send_message(message.from_user.id, text = 'Узнать наличный курс',
                            reply_markup=markup)
    bot.register_next_step_handler(msg, process_coin_step)#Убирает клавиатуру

def process_coin_step (message):
    try:
        markup = types.ReplyKeyboardRemove(Selective = True)
        # Получив сообщение с этим объектом, 
        # клиенты Telegram удалят текущую пользовательскую клавиатуру и 
        # отобразят буквенную клавиатуру по умолчанию.
        for coin in response:
            if (message.text == coin ['CharCode']):
                bot.send_message(message.from_user.id, printCoin(coin ['Nominal'], coin ['Name'],
                                                     coin['Value']),
                reply_markup=markup, parse_mode="Markdown")
    except Exception:
        bot.reply_to(message, 'ooops')
        # В блоке try мы выполняем инструкцию, которая может породить исключение,
        #  а в блоке except мы перехватываем их. 
def printCoin(Nominal, Name, Value):
    '''Вывод курса пользователю'''
    return str (Nominal) + str (Name)+ '=' + str(Value) + ' рублей'


bot.enable_save_next_step_handlers(delay=2)
if __name__ == '__main__':
    bot.polling(non_stop=True)