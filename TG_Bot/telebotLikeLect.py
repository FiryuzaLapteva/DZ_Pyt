import telegram
from telegram import Update  #pip install python-telegram-bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
from mySupersecretToken import Get_my_Tg_taken
# развернула этот код на сервере https://www.pythonanywhere.com/
# по вот этой инструкции https://blog.pythonanywhere.com/148/

def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close() 

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Hi {update.effective_user.first_name}!"\
    "\n I can make some calculations for you."\
    "\nJust type /calcInt 2 + 1 if you want to make calculation with integer numbers. \n"\
    "\nType /calcR 2.1 + 1.3 if you want to make calculation with rational numbers. \n"\
    "\n As well I can make calculations with complex numbers."\
    "\nJust type /calcC (1+1j) + (1+1j) \n")

def CalculatorInt(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)

    x = int(context.args[0])
    action = context.args[1]
    y = int(context.args[2])

    if action == "+":
        update.message.reply_text(f'{x} {action} {y} = {x + y}')
    elif action == "-":
        update.message.reply_text(f'{x} {action} {y} = {x - y}')
    elif action == "*":
        update.message.reply_text(f'{x} {action} {y} = {x * y}')
    elif action == "/":
        update.message.reply_text(f'{x} {action} {y} = {x / y}')

def CalculatorRat(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)

    x = float(context.args[0])
    action = context.args[1]
    y = float(context.args[2])

    if action == "+":
        update.message.reply_text(f'{x} {action} {y} = {x + y}')
    elif action == "-":
        update.message.reply_text(f'{x} {action} {y} = {x - y}')
    elif action == "*":
        update.message.reply_text(f'{x} {action} {y} = {x * y}')
    elif action == "/":
        update.message.reply_text(f'{x} {action} {y} = {x / y}')

def CalculatorComplex(update: Update, context: CallbackContext):
    # 19:24; число 1: (1+1j);число 2: (1+1j); операция: +; результат: (2+2j)
    log(update, context)
    msg = update.message.text
    print(msg)

    x = complex(context.args[0])

    action = context.args[1]
    y = complex(context.args[2])

    if action == "+":
        update.message.reply_text(f'{x} {action} {y} = {x + y}')
    elif action == "-":
        update.message.reply_text(f'{x} {action} {y} = {x - y}')
    elif action == "*":
        update.message.reply_text(f'{x} {action} {y} = {x * y}')
    elif action == "/":
        update.message.reply_text(f'{x} {action} {y} = {x / y}')

updater = Updater(Get_my_Tg_taken())

# обработка команды старт (создаем Inline клавиатуру)
def startCommand(update: Update, context: CallbackContext):
    buttonA = telegram.InlineKeyboardButton('help', callback_data='buttonA')
    buttonB = telegram.InlineKeyboardButton('calculator integer', callback_data='buttonB')
    buttonC = telegram.InlineKeyboardButton('calculator rational', callback_data='buttonC')
    buttonD = telegram.InlineKeyboardButton('calculator complex', callback_data='buttonD')
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
        query.edit_message_text(text='Хотите узнать, что я умею? Нажмите /help')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Хотите произвести арифметическую операцию c целыми числами?'\
            '\nВведите /calcInt число1 операция число2. \n Например: /calcInt 2 + 1'\
            '\nОперацию выделите пробелом с двух сторон')
    
    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Хотите произвести арифметическую операцию c рациональными числами?'\
            '\nВведите /calcR число1 операция число2. \n Например: /calcInt 2.2 + 1.1'\
            '\nОперацию выделите пробелом с двух сторон')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_text(text='Хотите произвести арифметическую операцию c комплексными числами?'\
            '\nВведите /calcC число1 операция число2. \nНапример: /calcC (1+1j) + (1+1j)'\
            '\nКомлексные числа записывайте в скобках без пробелов.'\
            '\nОперацию над ними выделите пробелом с двух сторон')


updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('start', startCommand))
updater.dispatcher.add_handler(CommandHandler('calcInt', CalculatorInt))
updater.dispatcher.add_handler(CommandHandler('calcC', CalculatorComplex))
updater.dispatcher.add_handler(CommandHandler('calcR', CalculatorRat))
updater.dispatcher.add_handler(CallbackQueryHandler(callback=callback, pattern=None, run_async=False)
)

print(' server start \n To cancel Ctr + C')
updater.start_polling()
updater.idle()

