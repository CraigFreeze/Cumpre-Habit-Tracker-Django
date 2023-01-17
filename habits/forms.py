from django import forms

class ResponseForm(forms.Form):
    response = forms.CharField(
        max_length=1,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )