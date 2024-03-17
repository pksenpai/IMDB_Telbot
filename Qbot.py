import logging
from typing import Final # convert a variable to a constant
from decouple import config
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, filters
from telegram.ext import CommandHandler, MessageHandler, InlineQueryHandler


""" \_____________________________[CONSTS]_____________________________/ """
TOKEN: Final = config('TOKEN', cast=str)


""" \______________________________[LOGS]_____________________________/ """
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST request being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


""" \_____________________________[INF_FUNCS]_____________________________/ """
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = \
        """
        Hello {}, you are my best friend!
        what can i do for you? /help
        """.format(update.effective_user.first_name)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.effective_message.id,
        text=text,
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = \
        """
        ___
        [/1] >>> Upper & Lower words
        [/2] >>> Movie's Searcher🎥
        [/3] >>> Language Translator👽
        [/4] >>> Profile Card🖼
        [/5] >>> coming soon...
        [/6] >>> coming soon...
        """

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.effective_message.id,
        text=text,
    )


async def about001(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = \
        """
        If you want to convert all text letters to Uppercase or Lowercase:
        1. Write @{} before your text...
        2. After writing your text, choose Uppercase or Lowercase option!
        """.format(context.bot.username)
        
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.effective_message.id,
        text=text,
    )

async def about002(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = \
        """
        coming soon...
        """
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.effective_message.id,
        text=text,
    )

async def about003(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = \
        """
        coming soon...
        """
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.effective_message.id,
        text=text,
    )

async def about004(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = \
        """
        coming soon...
        """
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.effective_message.id,
        text=text,
    )


""" \_____________________________[ACT_FUNCS]_____________________________/ """
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


""" \_____________________________[INIT]_____________________________/ """
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    start_handler  = CommandHandler('start', start)
    help_handler   = CommandHandler('help', help)

    about001_handler   = CommandHandler('1', about001)
    about002_handler   = CommandHandler('2', about002)
    about003_handler   = CommandHandler('3', about003)
    about004_handler   = CommandHandler('4', about004)

    inline_handler = InlineQueryHandler(inlineHandle)

    app.add_handler(start_handler)
    app.add_handler(help_handler)

    app.add_handler(about001_handler)
    app.add_handler(about002_handler)
    app.add_handler(about003_handler)
    app.add_handler(about004_handler)

    app.add_handler(inline_handler)


    app.run_polling() # keep running like a loop...

