from django.contrib import admin
from habits.models import Habit, HabitResponse, HabitJournal

# Register your models here.
class HabitAdmin(admin.ModelAdmin):
    pass

class HabitResponseAdmin(admin.ModelAdmin):
    pass

class HabitJournalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Habit, HabitAdmin)
admin.site.register(HabitResponse, HabitResponseAdmin)
admin.site.register(HabitJournal, HabitJournalAdmin)