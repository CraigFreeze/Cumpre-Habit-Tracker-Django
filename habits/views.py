from django.shortcuts import render
from django.http import HttpResponseRedirect
from habits.models import Habit, HabitResponse, HabitJournal
from .forms import DayTrackerForm, CreateHabitForm, CreateHabitResponseForm, JournalHabitForm
from datetime import date

# View for the homepage
def habit_index(request):
    habits = Habit.objects.all() #This is needed to load dropdown of habits

    if request.method == 'POST':
        if 'delete' in request.POST: #checks if the delete button is pressed
            habit_id = request.POST.get('delete')
            habit = Habit.objects.get(id = habit_id).delete()
    context = {
        'habits': habits
    }
    return render(request, 'habit_index.html', context)

# Prepare content to be displayed for each individual habit
def habit_detail(request, pk):
    habits = Habit.objects.all()
    habit = Habit.objects.get(pk=pk)

    if request.method == 'POST':
        if 'submitResponse' in request.POST: # checks if button pressed is submit
            form = DayTrackerForm(request.POST)
            
            if form.is_valid(): #Cycles through characters and updates database
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

        elif 'createResponse' in request.POST: # checks if button pressed is submit
            form = CreateHabitResponseForm(request.POST)
            newResponse = HabitResponse(
                habit = habit,
                response_char = 'N', # sets default value to neither
                report_day = date.today()
            )
            newResponse.save()

    habitResponses = HabitResponse.objects.filter(habit=habit)

    # Creates a list of forms with preset values. This needs to be done in the view, so that we have hr.id
    forms = [DayTrackerForm(initial={'response_id': hr.id, 'response_char': hr.response_char}) for hr in habitResponses]

    context = {
        'habits': habits,
        'habit': habit,
        'forms' : forms
    }

    return render(request, 'habit_detail.html', context)

# Make new habits
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

# Create Journal Entries and provide template with journal data
def habit_journal(request):
    habits = Habit.objects.all()
    journalEntries = HabitJournal.objects.all()
    if request.method == 'POST':
        if 'delete_entry' in request.POST:
            entry_id = request.POST.get('delete_entry')
            HabitJournal.objects.get(id = entry_id).delete()

        form = JournalHabitForm(request.POST)
        if form.is_valid():
            if 'publish_entry' in request.POST:
                newEntry = HabitJournal(
                    title = form.cleaned_data["title"],
                    entry = form.cleaned_data["entry"],
                    report_day = date.today()
                )
            newEntry.save()
            return HttpResponseRedirect('/habits/journal')
    else:
        form = JournalHabitForm()

    context = {
        'habits': habits,
        'form': form,
        'journalEntries' : journalEntries
    }
    return render(request, 'habit_journal.html', context)