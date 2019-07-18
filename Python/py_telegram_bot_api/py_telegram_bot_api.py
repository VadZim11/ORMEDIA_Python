import telebot
from my_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Привет, мой создатель")
    elif message.text == "Пока":
        bot.send_message(message.chat.id, "Прощай, создатель")

bot.polling()