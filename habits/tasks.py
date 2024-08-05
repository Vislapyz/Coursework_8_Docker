from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def habit_push():
    """Отправка сообщения из бота в Телеграм с напоминанием о привычке"""
    habits = Habit.objects.all().order_by("time")
    current_time = datetime.now().time()
    for habit in habits:
        if habit.user.tg_chat_id and habit.time > current_time:
            tg_chat_id = habit.user.tg_chat_id
            message = habit.__str__()
            send_telegram_message(tg_chat_id, message)
        else:
            print("Нет привычек")
