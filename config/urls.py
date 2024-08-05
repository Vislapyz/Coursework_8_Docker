from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("habits/", include(("habits.urls", "habits"), namespace="habits")),
    path("users/", include(("users.urls", "users"), namespace="users")),
]
