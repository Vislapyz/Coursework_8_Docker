from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    """
    Создания экземпляра модели Habit
    """

    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitUpdateAPIView(UpdateAPIView):
    """
    Редактирования экземпляра модели Habit
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(DestroyAPIView):
    """
    Удаления экземпляра модели Habit
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitListAPIView(ListAPIView):
    """
    Вывод всех экземпляров модели Habit
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user).order_by("id")


class HabitRetrieveAPIView(RetrieveAPIView):
    """
    Вывод одного экземпляра модели Habit
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class PublicHabitListAPIView(ListAPIView):
    """
    Просмотр всех публичных привычек
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CustomPagination

    def get_queryset(self):
        """
        Отображения только публичных привычек.
        """
        return Habit.objects.filter(is_public=True).order_by("id")
