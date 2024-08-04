from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Привычки и его свойства"""

    owner = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        related_name="Привычки",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    place = models.CharField(
        max_length=256,
        verbose_name="Место",
        help_text="Введите место выполнения привычки",
        **NULLABLE,
    )
    time = models.TimeField(
        verbose_name="Время", help_text="Введите время выполнения привычки"
    )
    action = models.CharField(
        max_length=256,
        verbose_name="Действие",
        help_text="Введите действие, которое нужно выполнить",
    )
    is_pleasant_habit = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    associated_habit = models.ForeignKey(
        "self",
        verbose_name="Связанная приятная привычка",
        on_delete=models.SET_NULL,
        help_text="Данные признак указывается только для Полезной привычки",
        **NULLABLE,
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Периодичность выполнения привычки для напоминания",
    )
    award = models.CharField(max_length=200, verbose_name="Вознаграждение", **NULLABLE)
    execution_time = models.PositiveSmallIntegerField(
        default=120,
        verbose_name="Длительность выполнения",
        help_text="Временя на выполнение полезной привычки в секундах ",
    )
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.owner} будет делать {self.action} в {self.time} в {self.place}"
