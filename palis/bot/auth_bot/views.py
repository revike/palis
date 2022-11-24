import time

import requests
import telebot
from django.urls import reverse
from rest_framework import status

from bot.auth_bot.keyboards_auth import key_start
from palis.settings import API_TOKEN, BACKEND_URL
from user.models import User

bot = telebot.TeleBot(token=API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    """Start command"""
    bot.send_message(message.chat.id, 'Добро пожаловать!',
                     reply_markup=key_start())


@bot.message_handler(content_types=['text'])
def register(message):
    """Register user"""
    if message.text == 'Зарегистрироваться':
        url = reverse('users:register')
        telegram_id = message.chat.id
        user = User.objects.filter(telegram_id=telegram_id)
        username = message.chat.username
        if not username:
            username = f'{int(time.time() * 10000)}'
        if not user:
            password = User.objects.make_random_password()
            data = {
                'username': f'{username}',
                'telegram_id': f'{telegram_id}',
                'password': f'{password}'
            }
            response = requests.post(f'{BACKEND_URL}{url}', data=data)
            if response.status_code == status.HTTP_201_CREATED:
                msg = f'{username}, вы успешно зарегистрированы. ' \
                      f'Дождитесь подтверждения вашей учетной записи'
                bot.send_message(message.chat.id, f'{msg}')
            else:
                bot.send_message(message.chat.id, f'{response.text}')
        else:
            url = reverse('users:user', kwargs={'pk': user.first().id})
            data = {'username': username}
            # login && update login
            response = requests.patch(f'{BACKEND_URL}{url}', data=data)
            print(response.text)
            bot.send_message(
                message.chat.id,
                f'{user.first().username}, Вы уже зарегистрированы')


@bot.message_handler(content_types=['text'])
def login(message):
    """Login user"""
