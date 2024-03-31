from decouple import config
from telebot import TeleBot
from telebot import types


TOKEN = config('TOKEN', cast=str)
bot = TeleBot(TOKEN)


from googletrans import Translator

def translator(text):
    translator = Translator()
    language = translator.detect(text).lang

    match language:
        case 'en':
            return translator.translate(text, 'fa').text
        case 'fa':
            return translator.translate(text, 'en').text
        case default:
            return "sorry, This language was not recognized!"


@bot.message_handler(commands=["start"])
def greeting(message: types.Message):
    user = message.from_user
    text = \
    f"""
    HELLO MY DEAR FRIEND {user.first_name}!😍\n
        I'm so nice to meet you!😘\n
        I am a friend who knows a lot of things!🧐\n
        So if you want to know about things like me,
        I will be happy to help!🥰\n
        So let's get started!🎉

        >>> send me /help to show what can i do <<<
    """
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["help"])
def help(message):

    text = \
    """
    ___
    [/1] >>> Movie's Searcher🎥
    [/2] >>> Language Translator👽
    [/3] >>> Profile Card🖼
    [/4] >>> coming soon...
    [/5] >>> coming soon...
    [/6] >>> coming soon...
    """

    keyboard = types.ReplyKeyboardMarkup(row_width=2)

    button1 = types.KeyboardButton(text="/1")
    button2 = types.KeyboardButton(text="/2")
    button3 = types.KeyboardButton(text="/3")
    button4 = types.KeyboardButton(text="/4")
    button5 = types.KeyboardButton(text="/5")
    button6 = types.KeyboardButton(text="/6")

    keyboard.add(
        button1,
        button2,
        button3,
        button4,
        button5,
        button6,
    )

    bot.reply_to(message, text, reply_markup=keyboard)

# @bot.message_handler(commands=["1"])
# def search_movie(message):
#     bot.send_message(message.chat.id, text)

# @bot.message_handler() # commands=["2"]
# def translate(message: types.Message):
#     bot.send_message(message.from_user.id, translator(message.text))


@bot.message_handler(commands=["2"])
def translate(message: types.Message):
    global translate_flag
    global first_time

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    translate = types.KeyboardButton(text="/translate")
    cancel = types.KeyboardButton(text="/cancel")

    keyboard.add(
        translate,
        cancel
    )

    first_time = True
    translate_flag = True

    bot.send_message(message.from_user.id, "translate?", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "/cancel")
def cancel_translation(message: types.Message):
    global translate_flag
    translate_flag = False
    bot.send_message(message.from_user.id, "Translation canceled.", reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.from_user.id, "More options -> /help")

@bot.message_handler(func=lambda message: translate_flag == True, content_types=["text"])
def process_translation(message: types.Message):
    global first_time
    if not first_time:
        result = translator(message.text)
        bot.send_message(message.from_user.id, result, reply_markup=types.ReplyKeyboardRemove())

    first_time = False

    text = \
    """
    Please enter the text you want to translate:
    You can cancel the translation anytime by clicking on -> /cancel
    """
    bot.send_message(message.from_user.id, text)

@bot.message_handler(commands=["3"])
def user_info(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button = types.KeyboardButton(
            text="Card",
            request_contact=True
        )

    kb.add(button)

    text = \
    """
    This command creates a card from your profile.
    If you want to use it, click on the 'Card' button...

    """

    bot.send_message(message.from_user.id, text, reply_markup=kb)


bot.infinity_polling()