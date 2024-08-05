from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Cоздание модели Пользователя"""

    username = None

    email = models.EmailField(
        max_length=150, unique=True, verbose_name="email", help_text="Введите email"
    )
    phone_number = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users_avatar",
        verbose_name="Аватар пользователя",
        help_text="Загрузите изображение",
        **NULLABLE
    )
    counter = models.CharField(
        max_length=100,
        verbose_name="Страна",
        help_text="Введите страну проживания",
        **NULLABLE
    )

    tg_chat_id = models.CharField(
        max_length=100,
        verbose_name="tg_chat_id",
        help_text="Enter chat ID",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользоаптель"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
