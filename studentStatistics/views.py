from django.shortcuts import render, redirect
from .forms import FilterForm
from studentform.models import Student, School_Cycle, Syllabus, Semester
from studenthistory.models import Course
from itertools import chain

from openpyxl import Workbook
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required
def filterGeneration(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            generation = form.cleaned_data['idCycle']
            return redirect('show-statistics', generation=generation.idCycle)
    else:
        form = FilterForm()

    return render(request, 'studentStatistics/statistics_search_page.html', {'form': form})

@login_required
def showStatistics(request, generation):
    calculate_percent = lambda x, total: int(x * 100 / total)

    gen = School_Cycle.objects.get(idCycle=generation)
    students = Student.objects.filter(admission_cycle=gen)

    registers_semesters = []
    last = [0, None]
    for student in students:
        begin, end = student.admission_cycle, student.last_cycle
        no_semesters = extractSemesters(begin, end)
        registers_semesters.append(no_semesters)

        if no_semesters > last[0]:
            last[0], last[1] = no_semesters, end

    if request.GET.get('status') or request.GET.get('last_cycle') or request.GET.get('semester'):
        select_status = request.GET.get('status', '')
        select_last_cycle = request.GET.get('last_cycle', '')
        select_semester = request.GET.get('semester', '')

        if select_semester:
            try:
                filtered, registers_semesters = filterStudents(int(select_semester), registers_semesters, students)
                students = students.filter(idStudent__in=filtered)
            except:
                print("Error: Por favor, ingrese un valor numérico para el filtro de semestres.")

        if select_last_cycle:
            last_period = ''
            last_year = ''
            try:
                last_period = select_last_cycle[-1]
                int(last_period)

                last_period = ''
                last_year = select_last_cycle
            except:
                if len(select_last_cycle) > 0:
                    last_period = select_last_cycle[-1]
                    last_year = select_last_cycle[:-1]

            students = students.filter(last_cycle__year__icontains=last_year, last_cycle__cycle_period__icontains=last_period)

        students = students.filter(status__status__icontains=select_status)

    # Save filtered students in session
    request.session['filtered_students'] = list(students.values_list('idStudent', flat=True))
    request.session['filtered_semesters'] = registers_semesters

    finish_students = students.filter(status__code_name='GD')
    graduated_students = students.filter(status__code_name='TT')
    art33_expelled_students = students.filter(status__code_name='BC')
    art35_expelled_students = students.filter(status__code_name='B5')
    
    if len(students) < 1:
        attached_students = attached_percent = finish_percent = graduated_percent = semesters = 0
    else:
        semesters = extractSemesters(gen, last[1])
        attached_students = extractAttachedStudents(students, registers_semesters)
        attached_percent = calculate_percent(attached_students, len(students))
        finish_percent = calculate_percent(len(finish_students), len(students))
        graduated_percent = calculate_percent(len(graduated_students), len(students))

    # Save statistics in session
    request.session['statistics'] = {
        'gen': f'{gen.year}{gen.cycle_period}',
        'no_students': len(students),
        'no_finished_students': len(finish_students),
        'finish_percent': finish_percent,
        'no_graduated': len(graduated_students),
        'graduated_percent': graduated_percent,
        'no_art33': len(art33_expelled_students),
        'no_art35': len(art35_expelled_students),
        'semesters': semesters,
        'attached_students': attached_students,
        'attached_percent': attached_percent
    }

    return render(request, 'studentStatistics/show_student_statistics.html', 
                  {'students': students, 'cycle': gen, 'semesters': semesters, 'no_students': len(students),
                   'no_finished_students': len(finish_students), 'finish_percent': finish_percent,
                   'no_graduated': len(graduated_students), 'graduated_percent': graduated_percent,
                   'no_art33': len(art33_expelled_students), 'no_art35': len(art35_expelled_students),
                   'semesters_list': registers_semesters, 'attached_students': attached_students,
                   'attached_percent': attached_percent})

@login_required
def exportStudentStatistics(request):
    workbook = Workbook()
    registers_sheet = workbook.active
    registers_sheet.title = "Registros"

    # Add headers
    registers_data = [
        ["Codigo", 
         "Nombre", 
         "Estatus", 
         "Admision", 
         "Ultimo Ciclo", 
         "Semestres"],
    ]

    # Add data
    filteredStudents = request.session.get('filtered_students', [])
    no_semesters = request.session.get('filtered_semesters', [])

    students = Student.objects.filter(idStudent__in=filteredStudents)
    for i, student in enumerate(students):
        registers_data.append(
            [student.code, 
             f'{student.name} {student.first_last_name} {student.second_last_name}', 
             student.status.status, 
             f'{student.admission_cycle.year}{student.admission_cycle.cycle_period}', 
             f'{student.last_cycle.year}{student.last_cycle.cycle_period}', 
             no_semesters[i]])

    # Add data to sheet
    for row in registers_data:
        registers_sheet.append(row)


    # Add statistics sheet
    statistics_sheet = workbook.create_sheet(title="Estadisticas")

    # Add headers
    statistics = request.session.get('statistics', {})
    statistics_data = [
        ["Generación", 
         "Semestres", 
         "No. Alumnos",
         "No. Alumnos que pertenecen",
         "%",
         "No. Egresados",
         "%",
         "No. Titulados",
         "%",
         "No. Bajas por Articulo 33",
         "No. Bajas por Articulo 35"],  # Header
    ]
    if statistics_data:
        statistics_data.append(
            [statistics['gen'],
            statistics['semesters'],
            statistics['no_students'],
            statistics['attached_students'],
            f'{statistics['attached_percent']}%',
            statistics['no_finished_students'],
            f'{statistics['finish_percent']}%',
            statistics['no_graduated'],
            f'{statistics['graduated_percent']}%',
            statistics['no_art33'],
            statistics['no_art35']]
        )

    # Add data
    for row in statistics_data:
        statistics_sheet.append(row)
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=estadisticas_estudiantes.xlsx'
    workbook.save(response)

    return response



def extractSemesters(CycleA, CycleB):
        year_a, letter_a = int(CycleA.year), CycleA.cycle_period
        year_b, letter_b = int(CycleB.year), CycleB.cycle_period

        semesters = (abs(year_b - year_a)) * 2

        if letter_a == 'A':
            semesters += 1
        if letter_b == 'B':
            semesters += 1

        return semesters

def filterStudents(filter, semesters, students):
    filtered_students = []
    semesters_list = []
    for i, student in enumerate(students):
        if semesters[i] == filter:
            filtered_students.append(student.idStudent)
            semesters_list.append(semesters[i])

    return filtered_students, semesters_list

def extractAttachedStudents(students, semesters):
    syllabus = students.first().syllabus
    syllabus_plan = Semester.objects.filter(syllabus=syllabus)
    attached_students = 0
    for i, student in enumerate(students):
        is_attached = True
        current_semester = semesters[i]
        plan_max_semesters = student.syllabus.semesters

        if current_semester > plan_max_semesters:
            is_attached = False
        else:
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