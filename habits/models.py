from django.db import models

# Create your models here.
class Habit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class HabitResponse(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    response_char = models.CharField(max_length=1) # G - Green // N - Neither // R - Red
    report_day = models.DateTimeField()