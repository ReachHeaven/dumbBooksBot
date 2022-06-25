import xml.etree.ElementTree as ET
from telebot import types
import telebot

def bot_core(minutes, genre):
    tree = ET.parse("books.xml")
    root = tree.getroot()

    for books in root.findall(f'.//{minutes}/*[@genre="{genre}"]'):
        title = books.get('title')
        link = books[0].text
        #bookdictionary[title] = link
        return (f"Вам подходит рассказ: {title}\nСсылка: {link}")

bot = telebot.TeleBot('5317163091:AAEqkf5QQXJTE1bZ9KBmXoumn7wv0ZpmYiU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ten = types.KeyboardButton("10 минут")
    twenty= types.KeyboardButton("20 минут")
    thirty = types.KeyboardButton('30 минут')
    fourty = types.KeyboardButton('40 минут')
    hour = types.KeyboardButton('1 час')
    markup.add(ten)
    markup.add(twenty)
    markup.add(thirty)
    markup.add(fourty)
    markup.add(hour)
    bot.send_message(message.chat.id, 'Привет, какое время ты готов потратить на чтение?', reply_markup=markup)
    bot.register_next_step_handler(message, handle_minutes_and_genre)

def handle_minutes_and_genre(message):
    global time

    if message.text == '10 минут':
        time = 'tenMinutes'
    elif message.text == '20 минут':
        time = 'twentyMinutes'
    elif message.text == '30 минут':
        time = 'thirtyMinutes'
    elif message.text == '40 минут':
        time = 'fourtyMinutes'
    elif message.text == '1 час':
        time = 'hour'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    fantastic = types.KeyboardButton("Фантастика")
    detective = types.KeyboardButton("Детектив")
    realism = types.KeyboardButton('Реализм')
    fantasy = types.KeyboardButton('Фэнтези')
    drama = types.KeyboardButton('Драма')
    markup.add(fantastic)
    markup.add(detective)
    markup.add(realism)
    markup.add(fantasy)
    markup.add(drama)
    bot.send_message(message.chat.id, text = 'Какой жанр тебе нравится?' , reply_markup=markup)
    bot.register_next_step_handler(message, genre_writer)


def genre_writer(message):
    global b_type

    if message.text == 'Фантастика':
        b_type = 'Фантастика'
    elif message.text == 'Детектив':
        b_type = 'Детектив'
    elif message.text == 'Реализм':
        b_type = 'Реализм'
    elif message.text == 'Фэнтези':
        b_type = 'Фэнтези'
    elif message.text == 'Драма':
        b_type = 'Драма'
    bot.send_message(message.chat.id, bot_core(time, b_type))
    bot.send_message(
                message.chat.id,
                f'Тыкни  /start '
                f'чтобы получить новый рассказ '
                )




bot.polling(none_stop=True, interval=0)


