from django import forms
from .models import Plan

class GetPlan(forms.ModelForm):

    class Meta:
        model = Plan
        fields = ('age_s', 'age_e', 'height_s', 'height_e', 'starting_weight_s', 
            'starting_weight_e', 'ending_weight_s', 'ending_weight_e', 'calories_s', 
            'calories_e', 'protein_s', 'protein_e', 'period_s', 'period_e', 'sex')