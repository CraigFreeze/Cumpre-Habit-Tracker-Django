from django.shortcuts import render
from django.http import HttpResponseRedirect
from habits.models import Habit, HabitResponse
from .forms import DayTrackerForm, CreateHabitForm, CreateHabitResponseForm, DeleteHabitForm
from datetime import date

# Create your views here.
def habit_index(request):
    habits = Habit.objects.all()
    form = DeleteHabitForm(request.POST)

    if request.method == 'POST':
        print("before is valid")
        if form.is_valid():
            print("validated")
            if 'delete' in request.POST:
                print("is delete")
                print(request.POST)
                habit_id = request.POST.get('delete')
                habit = Habit.objects.get(id = habit_id).delete() # TODO: THIS IS WHERE MY PROBLEM IS 
                print(habit)

    context = {
        'form': form,
        'habits': habits
    }
    return render(request, 'habit_index.html', context)

def habit_detail(request, pk):
    habits = Habit.objects.all()
    habit = Habit.objects.get(pk=pk)

    if request.method == 'POST':
        if 'submitResponse' in request.POST:
            form = DayTrackerForm(request.POST)
            
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
        elif 'createResponse' in request.POST:
            form = CreateHabitResponseForm(request.POST)
            newResponse = HabitResponse(
                habit = habit,
                response_char = 'N',
                report_day = date.today()
            )
            newResponse.save()

    habitResponses = HabitResponse.objects.filter(habit=habit)
    forms = [DayTrackerForm(initial={'response_id': hr.id, 'response_char': hr.response_char}) for hr in habitResponses]

    context = {
        'habits': habits,
        'habit': habit,
        # 'habitResponses' : habitResponses,
        'forms' : forms
    }

    return render(request, 'habit_detail.html', context)

def habit_create(request):
    habits = Habit.objects.all()
    if request.method == 'POST':
        form = CreateHabitForm(request.POST)
        if form.is_valid():
            newHabit = Habit(
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"]
            )
            newHabit.save()
            return HttpResponseRedirect('/habits/')
    else:
        form = CreateHabitForm()
    context = {
        'habits': habits,
        'form': form
    }
    return render(request, 'habit_create.html', context)
