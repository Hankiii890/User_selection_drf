from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """Класс управления созданием пользователей"""
    def create_user(self, email, password=None, **extra_fields):
        # Проверка на наличие почты
        if not email:
            raise ValueError("Поле email должно быть заполнено!")
        email = self.normalize_email(email)    # Нормализация email
        user = self.model(email=email, **extra_fields)   # Создание экземпляра пользователя
        user.set_password(password)    # Установка пароля
        user.save(using=self._db)    # Сохранение пользователя в базе данных
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Установка дополнительных полей для суперпользователя
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """Класс определения ролей пользователей"""
    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('manager', 'Менеджер'),
        ('crm_admin', 'CRM-менеджер'),
    )

    email = models.EmailField(unique=True)    # Поле для email с уникальным значением
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)    # Поле для роли
    offer = models.BooleanField(default=False)    # Поле для предложений
    avatar = models.ImageField(upload_to='avatars/', default='default.png')    # Поле, для загрузки фото пользователя

    objects = UserManager()    # Менеджер для модели пользователя

    USERNAME_FIELD = 'email'    # Поле для аутентификации
    REQUIRED_FIELDS = ['role']    # Обязательные поля для создания пользователя

    def __str__(self):
        return self.email    # Строковое представление пользователя
