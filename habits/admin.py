from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "owner",
        "place",
        "time",
        "action",
        "is_pleasant_habit",
        "associated_habit",
        "periodicity",
        "award",
        "execution_time",
        "is_public",
    )
    list_filter = ("owner",)
    search_fields = ("owner", "action")
