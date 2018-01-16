from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Plan
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'lightning/index.html')

class PlanListView(ListView):
    model = Plan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
