from django.urls import path
from . import views

urlpatterns = [
    path("", views.habit_index, name='habit_index'),
    path("<int:pk>/", views.habit_detail, name = "habit_detail"),
]