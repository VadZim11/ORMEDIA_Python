import telebot
from my_token import TOKEN
from rate_nbrb import get_money

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Привет!")
    elif message.text == "Пока":
        bot.send_message(message.chat.id, "Пока!")
    elif "курс" in message.text:
        bot.send_message(message.chat.id, get_money(message.text))
    else :
        bot.send_message(message.chat.id, "Ты что несешь?")

bot.polling()