from django.db import models

# This is the habits (represented as a card on screen)
class Habit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

# Each Individual reponse. It can be Green, Gray, or Red
class HabitResponse(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    response_char = models.CharField(max_length=1) # G - Green // N - Neither // R - Red
    report_day = models.DateTimeField()

# Data for the Journal tab
class HabitJournal(models.Model):
    title = models.CharField(max_length=100)
    entry = models.CharField(max_length=1000000) # G - Green // N - Neither // R - Red
    report_day = models.DateTimeField(max_length=10000)