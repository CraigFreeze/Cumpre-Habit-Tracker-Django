from django import forms
from habits.models import Habit, HabitResponse

class DayTrackerForm(forms.Form):
    response_id = forms.CharField(
        widget=forms.HiddenInput()
    )
    response_char = forms.CharField(
        widget=forms.HiddenInput()
    )

class HabitResponseForm(forms.Form):
    response_char = forms.CharField(max_length=1) # G - Green // N - Neither // R - Red
    #report_day = models.DateTimeField()
