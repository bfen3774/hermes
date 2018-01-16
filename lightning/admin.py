from django.contrib import admin

from .models import Plan, Diet, Food
# Register your models here.

admin.site.register(Plan)
admin.site.register(Diet)
admin.site.register(Food)