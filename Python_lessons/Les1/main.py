import telebot
import json
import time
import requests
import lxml.html
from lxml import etree
# import urllib
from telebot import types

# TOKEN = "1686386623:AAGYNYIbclNzlaS5NRcpCgIw8EucaL1rnZE"
bot = telebot.TeleBot('1686386623:AAGYNYIbclNzlaS5NRcpCgIw8EucaL1rnZE')

def get_titles(html_text):
    tree = lxml.html.document_fromstring(html_text)
    # extract text title from html, unique tag --> tags to text
    text_titles = tree.xpath("//*[@class='title']/a/text()")
    text_content = tree.xpath("//*[@class='col-sm-6 preview']/p/text()")
    return text_titles, text_content

def get_news_list():
    html_text = requests.get("https://etu.ru/")
    if html_text.status_code == 200:
        text_title, text_content = get_titles(html_text.text)
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        news = []
        for i, t in enumerate(text_title):
            news.append(types.InlineKeyboardButton(text=t, callback_data='{iter}'.format(iter=i))) #кнопка «Первой новости»
            keyboard.add(news[i]);    #добавляем кнопку в клавиатуру
        return keyboard

def help():
    msg = """Что умеет бот?
    /newslist  Загрузить список новостей
    /schedule  Загрузить расписание"""
    return msg    

def schedule():
    msg = "//В разработке"
    return msg


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/newslist":
        bot.send_message(message.from_user.id, 'Выберите тему:', reply_markup=get_news_list())
    elif message.text == "/schedule":
        bot.send_message(message.from_user.id, text=schedule())
    elif message.text == "/help":
        bot.send_message(message.from_user.id, text=help())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    html_text = requests.get("https://etu.ru/")
    if html_text.status_code == 200:
        text_title, text_content = get_titles(html_text.text)
    for i, t in enumerate(text_content):
        if call.data == str(i): 
            bot.send_message(call.message.chat.id, t)


# always at the end
bot.polling(none_stop=True, interval=0)


# def get_updates():
#    tg_request = requests.get(BOT_URL.format(method="getUpdates"))
#    try:
#        tg_req_data = json.loads(tg_request.text)
#        return tg_req_data
#    except Exception as e:
#        print(e)


# while True:
#    data = get_updates()
#    print(data)



# import requests
# import lxml.html
# from lxml import etree
#
#
# def get_titles(html_text):
#     tree = lxml.html.document_fromstring(html_text)
#     # extract text title from html, unique tag --> tags to text
#     text_titles = tree.xpath("//*[@class='title']/a/text()")
#     text_content = tree.xpath("//*[@class='col-sm-6 preview']/p/text()")
#     return text_titles, text_content
#
#
# html_text = requests.get("https://etu.ru/")
# if html_text.status_code == 200:
#     text_title, text_content = get_titles(html_text.text)
#     for i, t in enumerate(text_title):
#         text = """
#         Заголовок -- {title}
#         Контент   -- {content}
#         """.format(title = t, content = text_content[i])
#         print(text)