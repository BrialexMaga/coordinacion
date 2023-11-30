from django.shortcuts import render
from .forms import StudentCodeForm
from studentform.models import Student, Career
from .models import Course, School_Cycle, Subject
from collections import OrderedDict

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

import pickle
import numpy as np

def searchPage(request):
    if request.method == 'POST':
        form = StudentCodeForm(request.POST)
        if form.is_valid():
            student_code = form.cleaned_data['student_code']
            try:
                student = Student.objects.get(code=student_code)
                courses = Course.objects.filter(student=student).order_by('school_cycle__year', 'school_cycle__cycle_period', 
                                                                          'section__subject__key_subject', 'grade_period')
                career = Career.objects.get(idCareer=student.idCareer.idCareer)

                cycles_list = extractCycles(courses)
                risk_subjects, len_risk_subjects = extractRiskSubjects(courses, student)
                total_credits, remaining_credits = extractCredits(courses, student)
                average_score = extractAverageScore(courses)

                prediction = predictRisk(student)

                return render(request, 'studenthistory/show_history.html', 
                              {'student': student, 'prediction': prediction, 'courses': courses, 'cycles_list': cycles_list,
                               'risk_subjects': risk_subjects, #'len_list': len_list, 'len_cycles': len_cycles,
                               'len_risk_subjects': len_risk_subjects, 'career': career, 'total_credits': total_credits,
                               'remaining_credits': remaining_credits, 'average_score': average_score})
            except Student.DoesNotExist:
                form.add_error('student_code', 'No se encontró ningún estudiante con este código.')
    else:
        form = StudentCodeForm()

    return render(request, 'studenthistory/search_page.html', {'form': form})







def extractAverageScore(courses):
    divider = 0
    score = 0
    for course in courses:
        if course.grade > 59:
            score += course.grade
            divider += 1
    
    average_score = score / divider

    return average_score


def extractCredits(courses, student):
    total_credits = 0
    for course in courses:
        if course.grade > 59:
            total_credits += course.section.subject.credits
    
    remaining_credits = abs(total_credits - student.idCareer.needed_credits)

    return total_credits, remaining_credits


def extractCycles(courses):
    cycles = []
    cycles_index_list = courses.values_list('school_cycle__idCycle', flat=True).distinct()
    for cycleId in cycles_index_list:
        cycle = School_Cycle.objects.get(idCycle=cycleId)
        cycles.append(cycle)

    cycles = list(OrderedDict.fromkeys(cycles))
    return cycles

def extractRiskSubjects(courses, student):
    subject_indexes = courses.values_list('section__subject__idSubject', flat=True).distinct()
    subjects_indexes = list(set(subject_indexes))

    today_date = datetime.now().date()
    risk_courses = []
    for index in subjects_indexes:
        subject_registers = Course.objects.filter(student=student, 
                                                  section__subject__idSubject = index).order_by('school_cycle__year', 
                                                                                                'school_cycle__cycle_period', 
                                                                                                'grade_period')
        subject_info = Subject.objects.get(idSubject=index)

        if subject_info.has_extraordinary:
            ordinary = subject_registers.filter(grade_period__code_name = 'OE')
            extraordinary = subject_registers.filter(grade_period__code_name = 'E')

            if len(ordinary) > 1:
                # Determine by secuence
                if len(ordinary) == len(extraordinary):
                    last_extraordinary = extraordinary.last()
                    if last_extraordinary.grade < 60:
                        risk_courses.append(subject_info)
                else:
                    last_ordinary = ordinary.last()
                    if len(extraordinary) > 0:
                        last_extraordinary = extraordinary.last()
                        if last_ordinary.school_cycle == last_extraordinary.school_cycle:
                            if last_extraordinary.grade < 60:
                                risk_courses.append(subject_info)
                        else:
                            if last_ordinary.grade < 60:
                                risk_courses.append(subject_info)
                    else:
                        if last_ordinary.grade < 60:
                            risk_courses.append(subject_info)
            else:
                # Determine by one take and cycle
                if len(extraordinary) > 0:
                    last_extraordinary = extraordinary.last()
                    threshold = last_extraordinary.upload_date + relativedelta(months=5)
                    #threshold = last_extraordinary.upload_date + timedelta(days=1)
                    if last_extraordinary.grade < 60:
                        if last_extraordinary.school_cycle != student.last_cycle and threshold <= today_date:
                            risk_courses.append(subject_info)
                else:
                    last_ordinary = ordinary.last()
                    threshold = last_ordinary.upload_date + relativedelta(months=5)
                    #threshold = last_ordinary.upload_date + timedelta(days=1)
                    if last_ordinary.grade < 60:
                        if last_ordinary.school_cycle != student.last_cycle and threshold <= today_date:
                            risk_courses.append(subject_info)

        else:
            last_register = subject_registers.last()
            threshold = last_register.upload_date + relativedelta(months=5)
            #threshold = last_register.upload_date + timedelta(days=1)
            if len(subject_registers) > 1 and last_register.grade < 60:
                risk_courses.append(subject_info)
            elif len(subject_registers) == 1 and last_register.grade < 60 and last_register.school_cycle != student.last_cycle and threshold <= today_date:
                risk_courses.append(subject_info)                
    
    return risk_courses, len(risk_courses)


def predictRisk(student):
    model_path = 'IAmodels/IAmodel.pkl'
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    # Supongamos que tienes un método para obtener el vector de características del estudiante
    feature_vector = getFeatureVector(student)

    # Realiza la predicción
    #prediction = model.predict(np.array([feature_vector]))

    # Devuelve la predicción (puedes ajustar esto según cómo esté estructurado tu modelo)
    #return prediction[0]
    return 0


def getFeatureVector(student):
    return 0