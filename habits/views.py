from django.shortcuts import render
from habits.models import Habit, HabitResponse
from .forms import DayTrackerForm, HabitResponseForm

# Create your views here.
def habit_index(request):
    habits = Habit.objects.all()
    context = {
        'habits': habits
    }
    return render(request, 'habit_index.html', context)

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)

    if request.method == 'POST':
        form = DayTrackerForm(request.POST)
        #// Todo: hide the hidden field on the form 
        # Todo: FIX CSS styling on form // 
        # Todo: update color styling based on response char
        #// Todo: provide the default value for the response_id in the form. (populate the hidden form for the user)
        #? get vs post in line 16 ?
        #? learn how to make a branch and start saving to it (consider saving things straight to the main branch)?
        #Cycles through characters and updates database
        if form.is_valid():
            # N - Neither // G - Green // R - Red
            hr = HabitResponse.objects.get(id=form.cleaned_data['response_id'])
            if hr.response_char == 'N':
                hr.response_char = 'G'
            elif hr.response_char == 'G':
                hr.response_char = 'R'
            elif hr.response_char == 'R':
                hr.response_char = 'N'
            else: 
                print("not an accepted character")
            hr.save()

    habitResponses = HabitResponse.objects.filter(habit=habit)
    forms = [DayTrackerForm(initial={'response_id': hr.id, 'response_char': hr.response_char}) for hr in habitResponses]

    context = {
        'habit': habit,
        # 'habitResponses' : habitResponses,
        'forms' : forms
    }

    return render(request, 'habit_detail.html', context)
