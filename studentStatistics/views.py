from django.shortcuts import render
from .forms import FilterForm
from studentform.models import Student

def statisticSearchPage(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            generation = form.cleaned_data['idCycle']
            students = Student.objects.filter(admission_cycle=generation)
            return render(request, 'studentStatistics/show_student_statistics.html', 
                          {'students': students, 'cycle': generation})
    else:
        form = FilterForm()

    return render(request, 'studentStatistics/statistics_search_page.html', {'form': form})