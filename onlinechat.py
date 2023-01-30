import telebot
import os

import azuretranslation
import chat
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from dotenv import load_dotenv


load_dotenv()
sia = SentimentIntensityAnalyzer()

token = os.getenv('TGTOKEN')
bot = telebot.TeleBot(token)

user_dict = {}

class User:
    def __init__(self, name):
        self.name = name

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
    What's your name?
    """)
    bot.register_next_step_handler(msg, getusername)

def getusername(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        bot.send_message(chat_id, 'Nice to meet you ' + user.name)
        next = bot.send_message(chat_id, user.name + ' You may ask me some questions')
        bot.register_next_step_handler(next, converstion)
    except Exception as e:
        bot.reply_to(message, 'oooops')
        print(e)

def converstion(message):
    try:
        # print(message)
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        recieve_msg = azuretranslation.chitoeng(message.text)
        print(f"[{message.text}] {recieve_msg} \nsentiment score:{sia.polarity_scores(recieve_msg)}")
        sentimentscore(chat_id,recieve_msg)
        bot.send_chat_action(chat_id, action='typing')
        time.sleep(1)
        if not ("finish" or "end") in message.text:
            tochi = chat.chatfunc(recieve_msg)
            output = azuretranslation.engtochi(tochi)
            next = bot.send_message(chat_id, output)
            bot.register_next_step_handler(next, converstion)
        else:
            output = chat.chatfunc(recieve_msg)
            bot.send_message(chat_id, output)
            bot.send_message(chat_id, "Thanks for using")
    except Exception as e:
        bot.reply_to(message, 'oooops')
        print(e)

def sentimentscore(chat_id,message):
    sentimentsc = sia.polarity_scores(message)
    if(sentimentsc['compound'] < -0.3):
        bot.send_message(chat_id=os.getenv('ADMINID'),
        text=f"Alert!\n{chat_id} mentions:[{message}] \nsentiment score:{sentimentsc}")




# def converstion(message):
#     try:
#         chat_id = message.chat.id
#         name = message.text
#         user = User(name)
#         user_dict[chat_id] = user
#         recieve_msg = message.text
#         print(f"[{message.text}] sentiment score:{sia.polarity_scores(message.text)}")
#         sentimentscore(chat_id,message)
#         azuretranslation.engtochi(message.text)
#         if not ("finish" or "end") in message.text:
#             output = chat.chatfunc(recieve_msg)
#             next = bot.send_message(chat_id, output)
#             bot.register_next_step_handler(next, converstion)
#         else:
#             output = chat.chatfunc(recieve_msg)
#             bot.send_message(chat_id, output)
#             bot.send_message(chat_id, "Thanks for using")
#     except Exception as e:
#         bot.reply_to(message, 'oooops')
#         print(e)


bot.polling()