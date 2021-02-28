import telebot
import requests
import json
import time


# TOKEN = "1686386623:AAGYNYIbclNzlaS5NRcpCgIw8EucaL1rnZE"
bot = telebot.TeleBot('%1686386623:AAGYNYIbclNzlaS5NRcpCgIw8EucaL1rnZE%')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


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