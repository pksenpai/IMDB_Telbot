""" Global """
from decouple import config
from typing import Final # convert a variable to a constant
import logging

""" python-telegram-bot """
from telegram import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    filters,
    CommandHandler,
    MessageHandler,
    InlineQueryHandler,
)
from telegram.constants import ParseMode

""" Local """
from omdb_api import search_movie_by_title


""" \_____________________________[CONSTS]_____________________________/ """
TOKEN: Final = config('TOKEN', cast=str)
OMDB_URL: Final = config('OMDB_API_URL', cast=str)

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
        Hello <b>{}</b>, you are my best friend!
        what can i do for you? /help
        """.format(update.effective_user.first_name)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_to_message_id=update.effective_message.id,
        text=text,
        parse_mode=ParseMode.HTML,
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
        1. Write[ @{} ]before your text...
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
        If you want to search movies from IMDB:
        1. Write[ @{} search ]before your movie title...
        2. After writing your title, You can choose one of the found movies!
        3. Then you can see information about that movie!
        """.format(context.bot.username)

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

    query: str = inline_request.query
    if not query:
        return


    query_lst = query.split(' ', 1)
    try:
        if query_lst[0].strip() == 'search':
            if query := query_lst[1].strip():
                movies = search_movie_by_title(query)
                results = [
                    InlineQueryResultArticle(
                        id=movie.imdb_id,
                        title=movie.title,
                        input_message_content=InputTextMessageContent(
                            message_text=f"{movie.title} - {movie.year}:\n\n" + OMDB_URL + f"{movie.imdb_id}/"
                        ),
                        thumbnail_url=movie.poster,
                    )
                    for movie in movies
                ]

                await update.inline_query.answer(results, auto_pagination=True)
                return
    except IndexError:
        pass

    responses = [
            InlineQueryResultArticle(id='1', title="UpperCase", input_message_content=InputTextMessageContent(query.upper())),
            InlineQueryResultArticle(id='2', title="LowerCase", input_message_content=InputTextMessageContent(query.lower())),
            ]

    await inline_request.answer(responses)



""" \_____________________________[INIT]_____________________________/ """
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build() # init

    ''' StartOptions '''
    app.add_handler(CommandHandler('start', start)) # greeting
    app.add_handler(CommandHandler('help', help)) # show options

    ''' AboutOptions '''
    app.add_handler(CommandHandler('1', about001)) # Uppercase & Lowercase
    app.add_handler(CommandHandler('2', about002)) # Search Movies IMDB
    app.add_handler(CommandHandler('3', about003)) # Coming soon...
    app.add_handler(CommandHandler('4', about004)) # Coming soon...

    ''' InLines '''
    app.add_handler(InlineQueryHandler(inlineHandle)) # options /1 /2

    ''' LoopToEnd '''
    app.run_polling() # keep running like a loop...

