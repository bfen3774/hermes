from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Plan
from django.http import JsonResponse
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

    def get_queryset(self):
        minPeriod = self.request.GET.get('minPeriod')
        maxPeriod = self.request.GET.get('maxPeriod')
        if minPeriod:
            return Plan.objects.filter(period__gte=minPeriod).filter(period__lt=maxPeriod)
        else:
            return Plan.objects.all()
