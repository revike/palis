import telebot
from django.core.management import BaseCommand

from bot.auth_bot.handlers_auth import register, login
from bot.auth_bot.keyboards_auth import key_start
from palis.settings import API_TOKEN


class Command(BaseCommand):
    """Команда для создания супер юзера"""

    def handle(self, *args, **options):

        bot = telebot.TeleBot(token=API_TOKEN)

        @bot.message_handler(commands=['start'])
        def start_message(message):
            """Start command"""
            bot.send_message(message.chat.id, 'Добро пожаловать!',
                             reply_markup=key_start())

        @bot.message_handler(content_types=['text'])
        def running_bot(message):
            """Register user"""
            if message.text == 'Зарегистрироваться':
                register(bot, message)
            elif message.text == 'Войти':
                login(bot, message)
            else:
                bot.send_message(message.chat.id, 'Неверная команда...',
                                 reply_markup=key_start())

        bot.polling(none_stop=True)
