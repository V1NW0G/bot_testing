import telebot
import os

import chat
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

token = "5960383239:AAEvPLli6OVjGDTVrQ9VpURYVz7zjGO0pfw"
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
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        print(message.text)
        print(message)
        bot.send_message(chat_id, 'Nice to meet you ' + user.name)
        next = bot.send_message(chat_id, user.name + ' You may ask me some questions')
        bot.register_next_step_handler(next, converstion)
    except Exception as e:
        bot.reply_to(message, 'oooops')
        print(e)

def converstion(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        recieve_msg = message.text
        print(f"[{message.text}] sentiment score:{sia.polarity_scores(message.text)}")
        if not ("finish" or "end") in message.text:
            output = chat.chatfunc(recieve_msg)
            next = bot.send_message(chat_id, output)
            bot.register_next_step_handler(next, converstion)
        else:
            output = chat.chatfunc(recieve_msg)
            bot.send_message(chat_id, output)
            bot.send_message(chat_id, "Thanks for using")


    except Exception as e:
        bot.reply_to(message, 'oooops')
        print(e)

bot.polling()