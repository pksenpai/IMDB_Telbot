import logging
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes
from telegram.ext import CommandHandler

TOKEN = config('TOKEN', cast=str)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Hello, you are my best friend!"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    app.run_polling() # keep running like a loop...

