from django.core.management.base import BaseCommand
from user_selection.models import User


class Command(BaseCommand):
    help = "Создание пользователей"

    def handle(self, *args, **options):
        users = [
            {'email': 'user@gmail.com', 'role': 'user'},
            {'email': 'manager@gmail.com', 'role': 'manager'},
            {'email': 'crm_admin@gmail.com', 'role': 'crm_admin'},
        ]

        for user_data in users:
            User.objects.create_user(email=user_data['email'], role=user_data['role'])

        self.stdout.write(self.style.SUCCESS("Пользователи успешно созданы!"))
