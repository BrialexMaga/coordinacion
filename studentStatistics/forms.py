from django import forms
from studentform.models import School_Cycle

class FilterForm(forms.Form):
    ordered_cycles = School_Cycle.objects.all().order_by('-year', '-cycle_period')
    idCycle = forms.ModelChoiceField(queryset=ordered_cycles)