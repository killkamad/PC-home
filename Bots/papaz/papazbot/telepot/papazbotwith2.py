import time
import os
import json
import re
import asyncio
import random
import telepot
import telepot.aio
#from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardHide, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from time import strftime

async def on_chat_message(msg):

    global answerData, lowerFormulas
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    chat_id_str = str(chat_id)

# 'a' = append, сохраняем в блокноте 
    with open('papaz.log', 'a', encoding='utf8') as logFile:
        if content_type != 'text':
            return

        logFile.write('['+strftime("%Y-%m-%d %H:%M:%S")+'][' + chat_id_str + ' -> bot]: ' + msg['text'] + '\n')
        print('Chat:', content_type, chat_type, chat_id)
        print('Пльзователь '+ chat_id_str + ' написал:\n' +msg['text'].lower())
        request = msg['text']#.lower()
        
        if request in ('/start','hi','help','привет','помощь','старт','start'):
            await bot.sendMessage(chat_id, answerData['welcome'])#,reply_markup=rkh)
            logFile.write('['+strftime("%Y-%m-%d %H:%M:%S")+'][bot -> ' + chat_id_str + ']: ' + answerData['welcome'] + '\n')
            return
        elif request in ("Test1"):
            testAnswers = ["Pifagor",'Gerodot','Efklid','Arhimed','Ahmed','Otvet']
            inline_keyboard = []
            for a in range(len(testAnswers)):
                inline_keyboard.append([InlineKeyboardButton(text=testAnswers[a],callback_data=testAnswers[a])])
            ikm = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
            await bot.sendMessage(chat_id, 'Кто из древнегреческих математиков является чемпионом Олимпийских игр в кулачном бою и музыкантом?:', reply_markup=ikm)
        elif request in ("Test2"):
            testAnswers = ["(m*S)",'(m*a)','(S/t)','(a*b)','(da+da)','Tochno ne otvet']
            inline_keyboard = []
            for a in range(len(testAnswers)):
                inline_keyboard.append([InlineKeyboardButton(text=testAnswers[a],callback_data=testAnswers[a])])
            ikm = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
            await bot.sendMessage(chat_id, 'Выберите  формулы силы', reply_markup=ikm)
        elif request in answerData['formulas'].keys():
            se = random.randint(0, 1)
            phraseNumber = random.randint(0, 4)
            if se==0:
                add = answerData["addsToAnswer"]['start'][phraseNumber]
                await bot.sendMessage(chat_id, add + answerData['formulas'][request])
                logFile.write('['+strftime("%Y-%m-%d %H:%M:%S")+'][bot -> ' + chat_id_str + ']: ' + add + answerData['formulas'][request] + '\n')
            else:
                add = answerData["addsToAnswer"]['end'][phraseNumber]
                await bot.sendMessage(chat_id, answerData['formulas'][request] + "." + add)
                logFile.write('['+strftime("%Y-%m-%d %H:%M:%S")+'][bot -> ' + chat_id_str + ']: ' + answerData['formulas'][request] + add + '\n')
            return
        elif request in lowerFormulas:
            await bot.sendMessage(chat_id,  answerData["lowRequest"])
            logFile.write('['+strftime("%Y-%m-%d %H:%M:%S")+'][bot -> ' + chat_id_str + ']: ' + answerData["lowRequest"] + '\n')
            return
        elif request.lower() in ["тупой"]:
            await bot.sendMessage(chat_id,  "Сам ты такой! За шо ты так?")
            logFile.write('['+strftime("%Y-%m-%d %H:%M:%S")+'][bot -> ' + chat_id_str + ']: ' + "Сам ты такой! За шо ты так?" + '\n')
            return
        else:
            await bot.sendMessage(chat_id, answerData['badRequest'])


async def on_callback_query(msg):
    global answerData
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print(query_data)
    if query_data == answerData['formulas']['Test1']:
        await bot.sendMessage(from_id,  "Верно!, да ты жесткий")
    elif query_data == answerData['formulas']['Force']:
        await bot.sendMessage(from_id,  "Верно!, да ты жесткий")
    else:
        await bot.sendMessage(from_id,  "Неверно, мне стыдно за тебя, а я бот :(")


#tak tak sho mi tut delaem naverno zagruzhaem slovar
homeDir = os.path.dirname(__file__)
lowerFormulas = []
with open(os.path.join(homeDir, 'answersData.json'), encoding='utf8') as answerDataFile:
    print('Грузим ответы...')
    answerData = json.load(answerDataFile)
    for formula in answerData['formulas'].keys():
	    lowerFormulas.append(formula.lower())
    print('Ответы загружены. Да да я!')
			
TOKEN = '571531853:AAEoxiVANyVo7IYF-MEWFZwhnEPv5bfs3-w'

bot = telepot.aio.Bot(TOKEN)

loop = asyncio.get_event_loop()
#для получения данных от inline выбора добавляем callback_query и указываем фуекцию, которая будет срабатывать при ответах.
loop.create_task(bot.message_loop({'chat': on_chat_message, 'callback_query': on_callback_query}))
print('Listening ...')


loop.run_forever()



# nerabotaet
#while 1:
#   time.sleep(10)
