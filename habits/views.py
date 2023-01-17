from django.shortcuts import render
from habits.models import Habit, HabitResponse
from .forms import ResponseForm

# Create your views here.
def habit_index(request):
    habits = Habit.objects.all()
    context = {
        'habits': habits
    }
    return render(request, 'habit_index.html', context)

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)

    form = ResponseForm()
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = ResponseForm(
                response=form.cleaned_data["response"],
                habit=habit
            )
            response.save()

    habitResponses = HabitResponse.objects.filter(habit=habit)
    context = {
        'habit': habit,
        'habitResponses' : habitResponses,
    }

    return render(request, 'habit_detail.html', context)
