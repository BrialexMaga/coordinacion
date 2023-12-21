from django.shortcuts import render, redirect
from .forms import FilterForm
from studentform.models import Student, School_Cycle

def filterGeneration(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            generation = form.cleaned_data['idCycle']
            return redirect('show-statistics', generation=generation.idCycle)
    else:
        form = FilterForm()

    return render(request, 'studentStatistics/statistics_search_page.html', {'form': form})

def showStatistics(request, generation):
    calculate_percent = lambda x, total: int(x * 100 / total)

    cycles = School_Cycle.objects.all().order_by('year', 'cycle_period')
    gen = School_Cycle.objects.get(idCycle=generation)
    
    students = Student.objects.filter(admission_cycle=gen)

    if request.GET.get('status') or request.GET.get('last_cycle'):
        select_status = request.GET.get('status', '')
        select_last_cycle = request.GET.get('last_cycle', '')

        students = students.filter(status__status__icontains=select_status)

        if select_last_cycle:
            year, cycle_period = select_last_cycle[:-1], select_last_cycle[-1]
            students = students.filter(last_cycle__year=year, last_cycle__cycle_period=cycle_period)

    finish_students = students.filter(status__code_name='GD')
    graduated_students = students.filter(status__code_name='TT')
    art33_expelled_students = students.filter(status__code_name='BC')
    art35_expelled_students = students.filter(status__code_name='B5')

    registers_semesters = []
    last = [0, None]

    for student in students:
        begin, end = student.admission_cycle, student.last_cycle
        no_semesters = extractSemesters(begin, end)
        registers_semesters.append(no_semesters)

        if no_semesters > last[0]:
            last[0], last[1] = no_semesters, end
    
    semesters = extractSemesters(gen, last[1])

    if len(students) < 1:
        finish_percent = calculate_percent(len(finish_students), 1)
        graduated_percent = calculate_percent(len(graduated_students), 1)
    else:
        finish_percent = calculate_percent(len(finish_students), len(students))
        graduated_percent = calculate_percent(len(graduated_students), len(students))

    return render(request, 'studentStatistics/show_student_statistics.html', 
                  {'students': students, 'cycle': gen, 'semesters': semesters, 'no_students': len(students),
                   'no_finished_students': len(finish_students), 'finish_percent': finish_percent,
                   'no_graduated': len(graduated_students), 'graduated_percent': graduated_percent,
                   'no_art33': len(art33_expelled_students), 'no_art35': len(art35_expelled_students),
                   'semesters_list': registers_semesters})


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