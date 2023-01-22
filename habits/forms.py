from django import forms

class JournalHabitForm(forms.Form):
    title = forms.CharField(label='Title')
    entry = forms.CharField(label='Entry', widget=forms.TextInput(attrs={'class': 'form-control'}))

# Form that handles the habit responses.
class DayTrackerForm(forms.Form):
    response_id = forms.CharField(
        widget= forms.HiddenInput()
    )
    response_char = forms.CharField(
        widget= forms.HiddenInput()
    )

class CreateHabitForm(forms.Form):
    title = forms.CharField(label='Title')
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))

class CreateHabitResponseForm(forms.Form):
    report_day = forms.DateField(
        # widget= forms.HiddenInput()
    )