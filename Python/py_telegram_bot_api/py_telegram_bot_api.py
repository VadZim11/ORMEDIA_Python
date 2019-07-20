import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from my_token import TOKEN
from rate_nbrb import get_money

bot = telebot.TeleBot(TOKEN)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("USD", callback_data="USD"),
                InlineKeyboardButton("EUR", callback_data="EUR"),
                InlineKeyboardButton("RUB", callback_data="RUB"))
                #InlineKeyboardButton("ALL", callback_data="ALL"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "USD":
        bot.answer_callback_query(call.id, show_alert=True, text=get_money("курс USD"))
    elif call.data == "EUR":
        bot.answer_callback_query(call.id, show_alert=True, text=get_money("курс EUR"))
    elif call.data == "RUB":
        bot.answer_callback_query(call.id, show_alert=True, text=get_money("курс RUB"))
    elif call.data == "ALL":
        bot.answer_callback_query(call.id, show_alert=True, text=get_money("курс"))
        

@bot.message_handler(content_types=["text"])
def send_text(message):

    if message.text == "что я писал 5 сообщений назад":
        bot.send_message(message.chat.id, "Привет!")    
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Привет!")
    elif message.text == "Пока":
        bot.send_message(message.chat.id, "Пока!")
    elif "курс" in message.text:
        bot.send_message(message.chat.id, "Выбери валюту", reply_markup = gen_markup())
    else :
        bot.send_message(message.chat.id, "Ты что несешь?")

bot.polling()