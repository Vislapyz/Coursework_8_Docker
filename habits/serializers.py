from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    HabitAwardsValidator,
    DurationValidator,
    AssociatedHabitValidator,
    PleasantHabitAwardsValidator,
    PeriodicityValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            HabitAwardsValidator("associated_habit", "award"),
            DurationValidator("execution_time"),
            AssociatedHabitValidator("associated_habit"),
            PleasantHabitAwardsValidator("pleasant_habits", "award"),
            PeriodicityValidator("periodicity"),
        ]
