from django.shortcuts import render
from .forms import FilterForm
from studentform.models import Student, School_Cycle

def statisticSearchPage(request):
    calculate_percent = lambda x, total: int(x * 100 / total)
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            cycles = School_Cycle.objects.all().order_by('year', 'cycle_period')
            generation = form.cleaned_data['idCycle']

            students = Student.objects.filter(admission_cycle=generation)
            finish_students = students.filter(status__code_name='GD')
            graduated_students = students.filter(status__code_name='TT')
            art33_expelled_students = students.filter(status__code_name='BC')
            art35_expelled_students = students.filter(status__code_name='B5')

            semesters = extractSemesters(generation, cycles.last())
            finish_percent = calculate_percent(len(finish_students), len(students))
            graduated_percent = calculate_percent(len(graduated_students), len(students))
            return render(request, 'studentStatistics/show_student_statistics.html', 
                          {'students': students, 'cycle': generation, 'semesters': semesters, 'no_students': len(students),
                           'no_finished_students': len(finish_students), 'finish_percent': finish_percent,
                           'no_graduated': len(graduated_students), 'graduated_percent': graduated_percent,
                           'no_art33': len(art33_expelled_students), 'no_art35': len(art35_expelled_students)})
    else:
        form = FilterForm()

    return render(request, 'studentStatistics/statistics_search_page.html', {'form': form})




def extractSemesters(CycleA, CycleB):
        year_a, letter_a = int(CycleA.year), CycleA.cycle_period
        year_b, letter_b = int(CycleB.year), CycleB.cycle_period

        semesters = (abs(year_b - year_a)) * 2

        if letter_a == 'A':
            semesters += 1
        if letter_b == 'B':
            semesters += 1

        return semesters