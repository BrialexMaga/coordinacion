from django.shortcuts import render, redirect
from .forms import FilterForm
from studentform.models import Student, School_Cycle, Syllabus, Semester
from studenthistory.models import Course
from itertools import chain

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
    
    if len(students) < 1:
        attached_students = attached_percent = finish_percent = graduated_percent = semesters = 0
    else:
        semesters = extractSemesters(gen, last[1])
        attached_students = extractAttachedStudents(students, registers_semesters)
        attached_percent = calculate_percent(attached_students, len(students))
        finish_percent = calculate_percent(len(finish_students), len(students))
        graduated_percent = calculate_percent(len(graduated_students), len(students))

    return render(request, 'studentStatistics/show_student_statistics.html', 
                  {'students': students, 'cycle': gen, 'semesters': semesters, 'no_students': len(students),
                   'no_finished_students': len(finish_students), 'finish_percent': finish_percent,
                   'no_graduated': len(graduated_students), 'graduated_percent': graduated_percent,
                   'no_art33': len(art33_expelled_students), 'no_art35': len(art35_expelled_students),
                   'semesters_list': registers_semesters, 'attached_students': attached_students,
                   'attached_percent': attached_percent})




def extractSemesters(CycleA, CycleB):
        year_a, letter_a = int(CycleA.year), CycleA.cycle_period
        year_b, letter_b = int(CycleB.year), CycleB.cycle_period

        semesters = (abs(year_b - year_a)) * 2

        if letter_a == 'A':
            semesters += 1
        if letter_b == 'B':
            semesters += 1

        return semesters

def extractAttachedStudents(students, semesters):
    syllabus = students.first().syllabus
    syllabus_plan = Semester.objects.filter(syllabus=syllabus)
    attached_students = 0
    for i, student in enumerate(students):
        is_attached = True
        current_semester = semesters[i]
        current_plan = syllabus_plan.filter(number__lte=current_semester).order_by('number')
        should_have_subjects = list([semester.subject for semester in current_plan])

        j = 0
        while j < len(should_have_subjects):
            subject = should_have_subjects[j]
            courses = Course.objects.filter(student=student, section__subject=subject).order_by('school_cycle__year','school_cycle__cycle_period', 'grade_period')
            if len(courses) < 1:
                is_attached = False
                break
            else:
                if courses.last().grade == 'SD' or int(courses.last().grade) < 60:
                    is_attached = False
                    break
            
            j += 1
        
        if is_attached:
            attached_students += 1
        
    return attached_students