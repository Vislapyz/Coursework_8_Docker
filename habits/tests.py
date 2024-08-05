from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.test", password="test")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            place="test",
            time="01:00:00",
            action="Test",
        )

    def test_create_habit(self):
        """Cоздания привычки."""
        url = reverse("habits:habits-create")
        data = {
            "owner": self.user.pk,
            "place": "улица",
            "time": "06:00:00",
            "action": "пробежка",
        }
        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("owner"), self.user.pk)
        self.assertEqual(data.get("place"), "улица")
        self.assertEqual(data.get("time"), "06:00:00")
        self.assertEqual(data.get("action"), "пробежка")
        self.assertEqual(data.get("execution_time"), 120)

    def test_list_habit(self):
        """Вывода списка привычек."""
        response = self.client.get(reverse("habits:habits-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        """Удаления привычки."""
        url = reverse("habits:habits-destroy", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_habit(self):
        """Просмотра одной привычки."""
        url = reverse("habits:habits-retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("owner"), self.habit.owner.id)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("time"), self.habit.time)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_update_habit(self):
        """Изменения привычки."""
        url = reverse("habits:habits-update", args=(self.habit.pk,))
        data = {
            "user": self.user.pk,
            "place": "Улица",
            "time": "10:00:00",
            "action": "Пробежка 1 км",
        }
        response = self.client.put(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("owner"), self.habit.owner.id)
        self.assertEqual(data.get("place"), "Улица")
        self.assertEqual(data.get("time"), "10:00:00")
        self.assertEqual(data.get("action"), "Пробежка 1 км")

    def test_list_public_habit(self):
        """Вывода публичных привычек."""
        response = self.client.get(reverse("habits:public"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
