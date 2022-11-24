import telebot


def key_start():
    """First keyboard"""
    key = telebot.types.ReplyKeyboardMarkup(True)
    key.row('Зарегистрироваться', 'Войти')
    return key
