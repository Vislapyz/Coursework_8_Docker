from rest_framework import serializers
from rest_framework import exceptions


class HabitAwardsValidator:
    """Исключение одновременного выбора связанной привычки и указания вознаграждения"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        award = dict(value).get(self.field1)
        associated_habit = dict(value).get(self.field2)
        if award and associated_habit:
            raise exceptions.ValidationError(
                "Одновременный выбор связанной привычки и вознаграждения запрещен."
            )


class DurationValidator:
    """Проверка длительности выполнения задания"""

    def __init__(self, execution_time):
        self.execution_time = execution_time

    def __call__(self, value):
        if self.execution_time in value:
            execution_time = dict(value).get(self.execution_time)
            if int(execution_time) > 120:
                raise serializers.ValidationError(
                    "Время выполнения задания не должно превышать 120 секунд."
                )


class AssociatedHabitValidator:
    """Могут попадать только привычки с признаком приятной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        associated_habit = dict(value).get(self.field)
        if associated_habit and not associated_habit.is_pleasant_habit:
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только привычки "
                "с признаком приятной привычки."
            )


class PleasantHabitAwardsValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        associated_habit = dict(value).get("associated_habit")
        is_pleasant_habit = dict(value).get(self.field1)
        award = dict(value).get(self.field2)

        if award is not None and is_pleasant_habit is True:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения."
            )

        if is_pleasant_habit and associated_habit:
            raise serializers.ValidationError(
                "У приятной привычки не может быть признака связанной привычки."
            )


class PeriodicityValidator:
    """
    Проверяет чтобы нельзя было выполнять привычку реже, чем 1 раз в 7 дней и более 7 дней.
    """

    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, value):
        if self.periodicity in value:
            periodicity = dict(value).get(self.periodicity)
            if int(periodicity) > 7:
                raise serializers.ValidationError(
                    "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
                )
