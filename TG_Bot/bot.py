from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token('5926787797:AAGthxrg1MuCV7Qhy7cuhVkxkcflh4Et2mk').build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()