import time

import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from bot.auth_bot.keyboards_auth import key_start
from palis.settings import BACKEND_URL
from user.models import User


def register(bot, message):
    """Register user"""
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
            msg = f'@{username}, вы успешно зарегистрированы. ' \
                  f'Дождитесь подтверждения вашей учетной записи\n' \
                  f'Ваша пароль: {password}'
            bot.send_message(message.chat.id, f'{msg}')
        else:
            bot.send_message(message.chat.id, f'{response.text}')
    else:
        token, _ = Token.objects.get_or_create(user=user.first())
        url = reverse('users:user', kwargs={'pk': user.first().id})
        data = {'username': username}
        headers = {'Authorization': f'Token {token}'}
        response = requests.patch(f'{BACKEND_URL}{url}', data=data,
                                  headers=headers)
        msg = 'Вы уже зарегистрированы\n'
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            msg += 'Дождитесь подтверждения авторизации'
        bot.send_message(
            message.chat.id, f'@{user.first().username}, {msg}')


def login(bot, message):
    """Login user"""
    user = User.objects.filter(telegram_id=message.chat.id, is_active=True)
    if user:
        bot.send_message(message.chat.id, "Let's go")
    else:
        bot.send_message(
            message.chat.id, 'Вы еще не зарегистрированы или ваша '
                             'учетная запись не подтверждена',
            reply_markup=key_start())
