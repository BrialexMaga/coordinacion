from django.shortcuts import render, redirect
from .forms import byCycleForm, byCycleAndSubjectForm, byCycleRangeForm

def filterRateSubjectFailures(request):
    if request.method == 'POST':
        form = byCycleAndSubjectForm(request.POST)
        if form.is_valid():
            courses = form.filter_courses()
            # Puedes hacer algo con los cursos filtrados, como renderizarlos en el template
            #return render(request, 'rateSubjectFailures/by_cycle_subject.html', {'courses': courses})
    else:
        form = byCycleAndSubjectForm()
        form2 = byCycleForm()
        form3 = byCycleRangeForm()

    return render(request, 'rateSubjectFailures/failing_rate_filter.html', 
                  {'cycleRangeForm': form, 'cycleForm': form2, 'rangeForm': form3})

def byCycleFilter(request):
    if request.method == 'POST':
        form = byCycleForm(request.POST)
        if form.is_valid():
            courses = form.filter_courses()
            return render(request, 'rateSubjectFailures/by_cycle.html', {'courses': courses})

def byCycleSubjectFilter(request):
    if request.method == 'POST':
        form = byCycleAndSubjectForm(request.POST)
        if form.is_valid():
            courses = form.filter_courses()
            # Logica
            return render(request, 'rateSubjectFailures/by_cycle_subject.html', {'courses': courses})

def byCycleRangeFilter(request):
    if request.method == 'POST':
        form = byCycleRangeForm(request.POST)
        if form.is_valid():
            courses = form.filter_courses()
            return render(request, 'rateSubjectFailures/by_cycle_range.html', {'courses': courses})