import telebot
import config
from telebot import types
from config import admin_id
import time
import os
import logging
bot = telebot.TeleBot(config.token)

# logger = telebot.logger
# telebot.logger.basicConfig(filename='filename.log', level=logging.DEBUG,
#                     format=' %(asctime)s - %(levelname)s - %(message)s')

def send_to_admin():
    bot.send_message(admin_id, 'Меня запустили 	😃✈')


# @bot.message_handler(commands=['test'])
# def find_file_ids(message):
#     for file in os.listdir('schedule/'):
#         if file.split('.')[-1] == 'xlsx':
#             f = open('schedule/' + file, 'rb')
#             msg = bot.send_document(message.chat.id, f, None)
#             # А теперь отправим вслед за файлом его file_id
#             bot.send_message(message.chat.id, msg.document.file_id, reply_to_message_id=msg.message_id)
#         time.sleep(3)

# with open('papaz.log', 'a', encoding='utf8') as logFile:
#     if content_types != 'text':
#         return

@bot.message_handler(commands=['расписание'])
def command_handler(message):
    logging.info(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(True)
    markup.add('1 курс', '2 курс', '3 курс', '1 курс ТиПО')
    bot.send_message(message.chat.id, 'Выберете курс', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def schedule_handler(message):
    markup = types.ReplyKeyboardMarkup(True)
    markup.add('1 курс', '2 курс', '3 курс', '1 курс ТиПО')
    if message.text == 'Расписание':
        logging.info(str(message.chat.id) + ' ' + message.text)
        bot.send_message(message.chat.id, 'Выберете курс', reply_markup=markup)
        # bot.send_document(message.chat.id, doc)
    elif message.text == '1 курс':
        bot.send_message(message.chat.id, 'Держи друг')
        doc = open('./schedule/1course.xlsx', 'rb')
        bot.send_document(message.chat.id, doc, reply_markup=types.ReplyKeyboardRemove())
    elif message.text == '2 курс':
        bot.send_message(message.chat.id, 'Держи друг')
        doc = open('./schedule/2course.xlsx', 'rb')
        bot.send_document(message.chat.id, doc, reply_markup=types.ReplyKeyboardRemove())
    elif message.text == '3 курс':
        bot.send_message(message.chat.id, 'Держи друг')
        doc = open('./schedule/3course.xlsx', 'rb')
        bot.send_document(message.chat.id, doc, reply_markup=types.ReplyKeyboardRemove())
    elif message.text == '1 курс ТиПО':
        bot.send_message(message.chat.id, 'Держи друг')
        doc = open('./schedule/1courseTPO.xlsx', 'rb')
        bot.send_document(message.chat.id, doc, reply_markup=types.ReplyKeyboardRemove())



if __name__ == '__main__':
    # Избавляемся от спама в логах от библиотеки requests
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    # Настраиваем наш логгер
    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s', level=logging.INFO,
                        filename='bot_log.log', datefmt='%d.%m.%Y %H:%M:%S')
    send_to_admin()
    bot.infinity_polling()
