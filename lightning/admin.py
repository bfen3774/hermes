from django.contrib import admin

from .models import Plan, Workout, Diet, Food
# Register your models here.

admin.site.register(Plan)
admin.site.register(Workout)
admin.site.register(Diet)
admin.site.register(Food)