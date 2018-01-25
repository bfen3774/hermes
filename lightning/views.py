from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Plan
from django.utils import timezone
from django.http import HttpResponse
from .forms import GetPlan

# Create your views here.
def index(request):
    return render(request, 'lightning/index.html')

def get_plan(request):
    form = GetPlan()
    return render(request, 'blog/post_edit.html', {'form': form})

def filter_plans(request):

    if request.method == 'POST':
        plans = Plan.objects.filter(period__gte=period_s).filter(period__lt=period_e).filter(user_age__gte=age_s).filter(user_age__lt=age_e) \
                    .filter(user_height__gte=height_s).filter(user_height__lt=height_e).filter(user_starting_weight__gte=starting_weight_s).filter(user_starting_weight__lt=starting_weight_e) \
                    .filter(user_ending_weight__gte=ending_weight_s).filter(user_ending_weight__lt=ending_weight_e) \
                    .filter(calories__gte=calories_s).filter(calories__lt=calories_e).filter(macro_protein__gte=protein_s).filter(macro_protein__lt=period_e)

    return render(request, 'results.html', {'form': form, 'plans': plans})
class PlanListView(ListView):
    model = Plan
    #template_name = 'lightning/plan_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        return Plan.objects.all()

        ''' if self.request.is_ajax():
            age_s = self.kwargs['age_s']
            age_e = self.kwargs['age_e']
            height_s = self.kwargs['height_s']
            height_e = self.kwargs['height_e']
            starting_weight_s = self.kwargs['starting_weight_s']
            starting_weight_e = self.kwargs['starting_weight_e']
            ending_weight_s = self.kwargs['ending_weight_s']
            ending_weight_e = self.kwargs['ending_weight_e']
            calories_s = self.kwargs['calories_s']
            calories_e = self.kwargs['calories_e']
            protein_s = self.kwargs['protein_s']
            protein_e = self.kwargs['protein_e']
            period_s = self.kwargs['period_s']
            period_e = self.kwargs['period_e']

            plan_list = self.model.objects.filter(period__gte=period_s).filter(period__lt=period_e).filter(user_age__gte=age_s).filter(user_age__lt=age_e) \
                        .filter(user_height__gte=height_s).filter(user_height__lt=height_e).filter(user_starting_weight__gte=starting_weight_s).filter(user_starting_weight__lt=starting_weight_e) \
                        .filter(user_ending_weight__gte=ending_weight_s).filter(user_ending_weight__lt=ending_weight_e) \
                        .filter(calories__gte=calories_s).filter(calories__lt=calories_e).filter(macro_protein__gte=protein_s).filter(macro_protein__lt=period_e)
        else:
            plan_list = self.model.objects.all()
        return plan_list '''

'''     def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            age_s = self.kwargs['age_s']
            age_e = self.kwargs['age_e']
            height_s = self.kwargs['height_s']
            height_e = self.kwargs['height_e']
            starting_weight_s = self.kwargs['starting_weight_s']
            starting_weight_e = self.kwargs['starting_weight_e']
            ending_weight_s = self.kwargs['ending_weight_s']
            ending_weight_e = self.kwargs['ending_weight_e']
            calories_s = self.kwargs['calories_s']
            calories_e = self.kwargs['calories_e']
            protein_s = self.kwargs['protein_s']
            protein_e = self.kwargs['protein_e']
            period_s = self.kwargs['period_s']
            period_e = self.kwargs['period_e']

            plan_list = self.model.objects.filter(period__gte=period_s).filter(period__lt=period_e).filter(user_age__gte=age_s).filter(user_age__lt=age_e) \
                        .filter(user_height__gte=height_s).filter(user_height__lt=height_e).filter(user_starting_weight__gte=starting_weight_s).filter(user_starting_weight__lt=starting_weight_e) \
                        .filter(user_ending_weight__gte=ending_weight_s).filter(user_ending_weight__lt=ending_weight_e) \
                        .filter(calories__gte=calories_s).filter(calories__lt=calories_e).filter(macro_protein__gte=protein_s).filter(macro_protein__lt=period_e)
            data = serializers.serialize('json', plan_list)
        else:
            plan_list = self.model.objects.all()
        return HttpResponse( json.dumps(plan_list), content_type="application/json") '''
 