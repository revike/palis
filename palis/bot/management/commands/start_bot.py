from django.core.management import BaseCommand

from bot.auth_bot.views import bot


class Command(BaseCommand):
    """Команда для создания супер юзера"""

    def handle(self, *args, **options):
        bot.polling(none_stop=True)
