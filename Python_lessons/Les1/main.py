import telebot
import json
import time
import requests
import lxml.html
from lxml import etree
import urllib
import wget
import os
from telebot import types

# TOKEN = "1686386623:AAGYNYIbclNzlaS5NRcpCgIw8EucaL1rnZE"
bot = telebot.TeleBot('1686386623:AAGYNYIbclNzlaS5NRcpCgIw8EucaL1rnZE')

def get_titles(html_text):
    tree = lxml.html.document_fromstring(html_text)
    # extract text title from html, unique tag --> tags to text
    text_titles = tree.xpath("//*[@class='title']/a/text()")    
    return text_titles

def get_content(html_text):
    tree = lxml.html.document_fromstring(html_text)
    text_content = tree.xpath("//*[@class='col-sm-6 preview']/p/text()")
    return text_content

def get_titles_list():
    html_text = requests.get("https://etu.ru/")
    if html_text.status_code == 200:
        text_title = get_titles(html_text.text)
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        news = []
        for i, t in enumerate(text_title):
            #кнопка «Первой новости»
            news.append(types.InlineKeyboardButton(text=t, callback_data='{iter}'.format(iter=i)))
            keyboard.add(news[i]);    #добавляем кнопку в клавиатуру
        return keyboard

def help():
    msg = """Что умеет бот?
    /newslist  Загрузить список новостей
    /schedule  Загрузить расписание"""
    return msg    

def schedule():
    schedule_buttons = ['Excel' , '*.ics (Calendar)']
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    sched = []
    for i, t in enumerate(schedule_buttons):
        sched.append(types.InlineKeyboardButton(text=t, callback_data='{iter}'.format(iter=i+16)))
        keyboard.add(sched[i])
    return keyboard

def get_course_buttons():
    course_buttons = ['1','2','3','4','5 (+ Магистратура 1)','6 (+ Магистратура 2']
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    course = []
    for i, t in enumerate(course_buttons):
        course.append(types.InlineKeyboardButton(text=t, callback_data='{iter}'.format(iter=i+18)))
        keyboard.add(course[i])
    return keyboard

def get_faculty_buttons():
    faculty_buttons = ['ФРТ','ФЭЛ','ФКТИ','ФЭА','ФИБС','ИНПРОТЕХ', 'ГФ']
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    fuck = []
    for i, t in enumerate(faculty_buttons):
        fuck.append(types.InlineKeyboardButton(text=t, callback_data='{iter}'.format(iter=i+24)))
        keyboard.add(fuck[i])
    return keyboard

def definite_and_get_xls_file(courseGlobal, facultyGlobal, ThreedGlobal = 0):
    list_faculty = ('frt_','fel_','fkti_','fea_', 'fibs_', 'inproteh_', 'gf_')
    
    head = "https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/"
    tail = "?date=2021.03.09"
    #mid, temp
    for i, t in enumerate(list_faculty):
        if facultyGlobal == i:
            temp = t
    if ThreedGlobal != 0:
        mid = temp + str(courseGlobal) + '_' + str(ThreedGlobal) + ".xlsx"
    else:
        mid = temp + str(courseGlobal) + ".xlsx"

    link = head + mid + tail



    # scheduleDict = (FRT1='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/frt_1.xlsx?date=2021.03.09', 
    #                 FRT2='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/frt_2.xlsx?date=2021.03.09',
    #                 FEL1='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fel_1.xlsx?date=2021.03.09',
    #                 FEL2='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fel_2.xlsx?date=2021.03.09',
    #                 FKTI11='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fkti_1_1.xlsx?date=2021.03.09',
    #                 FKTI12='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fkti_1_2.xlsx?date=2021.03.09',
    #                 FKTI13='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fkti_1_3.xlsx?date=2021.03.09',
    #                 FKTI21='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fkti_2_1.xlsx?date=2021.03.09',
    #                 FKTI22='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fkti_2_2.xlsx?date=2021.03.09',
    #                 FKTI23='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fkti_2_3.xlsx?date=2021.03.09',
    #                 FEA1='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fea_1.xlsx?date=2021.03.09',
    #                 FEA2='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fea_2.xlsx?date=2021.03.09',
    #                 FIBS1='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fibs_1.xlsx?date=2021.03.09',
    #                 FIBS2='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fibs_2.xlsx?date=2021.03.09',
    #                 INPROTEH1='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/inproteh_1_2.xlsx?date=2021.03.09',
    #                 GF1='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/gf_1.xlsx?date=2021.03.09',
    #                 GF2='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/gf_2.xlsx?date=2021.03.09',
                    
    #                 FRT3='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/frt_3.xlsx?date=2021.03.09', 
    #                 FEL3='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fel_3.xlsx?date=2021.03.09',
    #                 FKTI31='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fkti_3_1.xlsx?date=2021.03.09',
    #                 FKTI32='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fkti_3_2.xlsx?date=2021.03.09',
    #                 FEA3='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fea_3.xlsx?date=2021.03.09',
    #                 FIBS3='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/fibs_3.xlsx?date=2021.03.09',
    #                 INPROTEH3='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/inproteh_3_4_1m.xlsx?date=2021.03.09',
    #                 GF3='https://etu.ru/assets/files/ru/studentam/raspisaniya-zanyatiy-i-ekzamenov/raspisanie/2020-2021-2/smeshannoe/gf_3.xlsx?date=2021.03.09' )
    wget.download(link, mid)
    print("")
    return mid

def delete_file(name):
    os.remove(name)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/newslist":
        bot.send_message(message.from_user.id, 'Выберите тему:', reply_markup=get_titles_list())
    elif message.text == "/schedule":
        bot.send_message(message.from_user.id, 'Выберите:', reply_markup=schedule())
    elif message.text == "/help":
        bot.send_message(message.from_user.id, text=help())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    #news
    if(call.data <= str(15)):
        html_text = requests.get("https://etu.ru/")
        if html_text.status_code == 200:
            text_content = get_content(html_text.text)
        for i, t in enumerate(text_content):
            if call.data == str(i): 
                bot.send_message(call.message.chat.id, t)
    
    #schedule Excel
    if(call.data == str(16)):
        bot.send_message(call.message.chat.id, 'Выберите:', reply_markup=get_course_buttons())
        #fileXls = definite_and_get_xls_file()

        
        #f = open("xd.xlsx","rb")
        #bot.send_document(message.chat.id,f)

    #schedule *.ics (Calendar)
    if(call.data == str(17)):
        print("17")

    #choose courses
    if(call.data >= str(18) and call.data <= str(23)):
        courseGlobal = int(call.data) - 17
        bot.send_message(call.message.chat.id, 'Выберите:', reply_markup=get_faculty_buttons())
    
    #choose faculty
    if(call.data >= str(24) and call.data <= str(30)):
        facultyGlobal = int(call.data) - 24
        
        # TODO definite_and_get_xls_file ARGS
        name = definite_and_get_xls_file(3, 2, 1)
        bot.send_document(call.message.chat.id, open(name, 'rb'))
        delete_file(name)



# always at the end
bot.polling(none_stop=True, interval=0)