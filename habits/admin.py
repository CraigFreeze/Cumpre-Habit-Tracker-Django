from django.contrib import admin
from habits.models import Habit, HabitResponse

# Register your models here.
class HabitAdmin(admin.ModelAdmin):
    pass

class HabitResponseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Habit, HabitAdmin)
admin.site.register(HabitResponse, HabitResponseAdmin)