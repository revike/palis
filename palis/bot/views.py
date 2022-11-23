import telebot

from palis.settings import API_TOKEN

bot = telebot.TeleBot(token=API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    """Start command"""
    bot.send_message(message.from_user.id, 'start')
