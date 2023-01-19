from django import forms
from habits.models import Habit, HabitResponse

class DayTrackerForm(forms.Form):
    response_id = forms.CharField(
        widget=forms.HiddenInput()
        # initial = HabitResponse.id
    )
    response_char = forms.CharField(
        widget=forms.HiddenInput()
        # initial = HabitResponse.id
    )

class HabitResponseForm(forms.Form):
    response_char = forms.CharField(max_length=1) # G - Green // N - Neither // R - Red
    #report_day = models.DateTimeField()

'''
<form method="post" >
    <input type="hidden" value = "{{ habitResponse.id }}" />
    <button class = "response" id="{{ habitResponse.id }}" type="submit"> 
        <!--onclick="cycleColor('{{ habitResponse.id }}', '{{habitResponse.response_char}}')"-->
        {{ habitResponse.response_char }}
    </button>
</form>
'''