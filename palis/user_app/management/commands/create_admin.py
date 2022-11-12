from django.core.management import BaseCommand

from palis.settings import ADMIN_LOGIN, ADMIN_PASSWORD, ADMIN_EMAIL
from user_app.models import User


class Command(BaseCommand):
    """Команда для создания супер юзера"""

    def handle(self, *args, **options):
        if not User.objects.filter(
                is_staff=True, is_superuser=True, is_active=True):
            User.objects.create_superuser(
                username=ADMIN_LOGIN, password=ADMIN_PASSWORD,
                email=ADMIN_EMAIL, is_active=True)
