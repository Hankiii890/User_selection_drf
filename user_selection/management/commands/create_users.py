from django.core.management.base import BaseCommand
from user_selection.models import User


class Command(BaseCommand):
    help = "Создание пользователей"

    def handle(self, *args, **options):
        # Создаем список пользователей для добавления в наше приложение
        users = [
            {'email': 'user@gmail.com', 'role': 'user'},
            {'email': 'manager@gmail.com', 'role': 'manager'},
            {'email': 'crm_admin@gmail.com', 'role': 'crm_admin'},
        ]

        # Проходимся по каждому пользователю и создаём его
        for user_data in users:
            User.objects.create_user(email=user_data['email'], role=user_data['role'])

        # Сообщение, после успешного создания
        self.stdout.write(self.style.SUCCESS("Пользователи успешно созданы!"))
