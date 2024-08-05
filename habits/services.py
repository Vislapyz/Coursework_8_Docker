import requests

from config.settings import BOT_TOKEN, TELEGRAM_URL


def send_telegram_message(tg_chat_id, message):
    """Отправляет сообщение в Телеграм через бота"""
    parameters = {"chat_id": tg_chat_id, "text": message}
    r = requests.get(f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", params=parameters)
    if r.status_code == 200:
        print("Сообщение отправлено")
    else:
        print("Ошибка отправки")
