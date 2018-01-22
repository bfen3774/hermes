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
        plan = Plan
        if self.request.is_ajax():
            age_s = self.get('age_s')
            age_e = request.GET.get('age_e')
            height_s = request.GET.get('height_s')
            height_e = request.GET.get('height_e')
            starting_weight_s = request.GET.get('starting_weight_s')
            starting_weight_e = request.GET.get('starting_weight_e')
            ending_weight_s = request.GET.get('ending_weight_s')
            ending_weight_e = request.GET.get('ending_weight_e')
            calories_s = request.GET.get('calories_s')
            calories_e = request.GET.get('calories_e')
            protein_s = request.GET.get('protein_s')
            protein_e = request.GET.get('protein_e')
            period_s = request.GET.get('period_s')
            period_e = request.GET.get('period_e')
            return plan.objects.filter(period__gte=period_s).filter(period__lt=period_e).filter(user_age__gte=age_s).filter(user_age__lt=age_e) \
                    .filter(user_height__gte=height_s).filter(user_height__lt=height_e).filter(user_starting_weight__gte=starting_weight_s).filter(user_starting_weight__lt=starting_weight_e) \
                    .filter(user_ending_weight__gte=ending_weight_s).filter(user_ending_weight__lt=ending_weight_e) \
                    .filter(calories__gte=calories_s).filter(calories__lt=calories_e).filter(macro_protein__gte=protein_s).filter(macro_protein__lt=period_e)
        else:
            return plan.objects.all()
