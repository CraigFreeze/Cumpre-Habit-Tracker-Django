from django.urls import path
from . import views

urlpatterns = [
    path("", views.habit_index, name='habit_index'),
    path("<int:pk>/", views.habit_detail, name = "habit_detail"),
    path("new", views.habit_create, name = "habit_create"),
    path("journal", views.habit_journal, name = "habit_journal"),
]