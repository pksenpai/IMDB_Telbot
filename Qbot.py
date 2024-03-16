import logging
from decouple import config
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes
from telegram.ext import CommandHandler, InlineQueryHandler

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

async def inlineHandle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    inline_request = update.inline_query
    if not inline_request:
        return

    query = inline_request.query
    if not query:
        return

    responses = [
            InlineQueryResultArticle(id='1', title="UpperCase", input_message_content=InputTextMessageContent(query.upper())),
            InlineQueryResultArticle(id='2', title="LowerCase", input_message_content=InputTextMessageContent(query.lower())),
            ]

    await inline_request.answer(responses)


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    inline_handler = InlineQueryHandler(inlineHandle)

    app.add_handler(start_handler)
    app.add_handler(inline_handler)


    app.run_polling() # keep running like a loop...

