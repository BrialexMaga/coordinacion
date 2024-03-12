from django.shortcuts import render
from .forms import StudentCodeForm
from studentform.models import Student, Career
from .models import Course, School_Cycle, Subject, CareerSubject
from collections import OrderedDict

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

from django.contrib.auth.decorators import login_required

import pickle
import pandas as pd
import numpy as np

from django.db import connection

@login_required
def searchPage(request):
    if request.method == 'POST':
        form = StudentCodeForm(request.POST)
        if form.is_valid():
            student_code = form.cleaned_data['student_code']
            try:
                student = Student.objects.select_related('idCareer').get(code=student_code)
                courses = Course.objects.select_related('student', 'school_cycle', 'section__subject').filter(student=student).order_by('school_cycle__year', 'school_cycle__cycle_period', 
                                                                          'section__subject__key_subject', 'grade_period')
                career = Career.objects.get(idCareer=student.idCareer.idCareer)

                has_courses = len(courses) > 0

                cycles_list, semesters = extractCycles(courses, student, has_courses)
                risk_subjects, len_risk_subjects = extractRiskSubjects(courses)
                total_credits, remaining_credits = extractCredits(courses, student)
                average_score = extractAverageScore(courses, has_courses)

                prediction, vector = predictRisk(student, courses, career, total_credits, remaining_credits, average_score, semesters)

                return render(request, 'studenthistory/show_history.html', 
                              {'student': student, 'prediction': prediction, 'courses': courses, 'cycles_list': cycles_list,
                               'risk_subjects': risk_subjects, 'vector': vector,  #'len_list': len_list, 'len_cycles': len_cycles,
                               'len_risk_subjects': len_risk_subjects, 'syllabus': student.syllabus, 'total_credits': total_credits,
                               'remaining_credits': remaining_credits, 'average_score': average_score})
            except Student.DoesNotExist:
                form.add_error('student_code', 'No se encontró ningún estudiante con este código.')
    else:
        form = StudentCodeForm()

    return render(request, 'studenthistory/search_page.html', {'form': form})







def gradeConverter(string):
    is_SD = False

    if string.upper() == 'SD':
        is_SD = True
        grade = 0
    else:
        try:
            grade = int(string)
        except ValueError:
            raise ValueError("La calificación no es válida. Debe ser 'SD' o un número entre 0 y 100.")

    return grade, is_SD

def extractAverageScore(courses, has_courses):
    average_score = 0
    if has_courses:
        divider = 0
        score = 0
        for course in courses:
            grade, is_SD = gradeConverter(course.grade)
            if not is_SD and grade > 59:
                score += grade
                divider += 1
        
        average_score = score / divider

    return round(average_score, 2)


def extractCredits(courses, student):
    total_credits = 0
    for course in courses:
        grade, is_SD = gradeConverter(course.grade)
        if not is_SD and grade > 59:
            total_credits += course.section.subject.credits
    
    remaining_credits = abs(total_credits - student.syllabus.needed_credits)

    return total_credits, remaining_credits


def extractCycles(courses, student, has_courses):
    cycles = []
    cycles_index_list = courses.values_list('school_cycle__idCycle', flat=True).distinct()
    for cycleId in cycles_index_list:
        cycle = School_Cycle.objects.get(idCycle=cycleId)
        cycles.append(cycle)

    cycles = list(OrderedDict.fromkeys(cycles))
    semesters = len(cycles)
    if has_courses:
        if cycles[-1] != student.last_cycle:
            semesters += 1
        
        return cycles, semesters

    return cycles, 1

def extractRiskSubjects(courses):
    subject_indexes = courses.values_list('section__subject__idSubject', flat=True).distinct()
    subject_indexes = list(set(subject_indexes))

    risk_courses = []
    for subject_index in subject_indexes:
        subject_ids = courses.values_list('section__subject__idSubject', flat=True).distinct()
        subjects = {subject.idSubject: subject for subject in Subject.objects.filter(idSubject__in=subject_ids)}

        #subject_info = Subject.objects.get(idSubject=subject_index)
        subject_info = subjects[subject_index]
        subject_courses = courses.filter(section__subject__idSubject=subject_index).order_by('school_cycle__year',
                                                                                             'school_cycle__cycle_period',
                                                                                             'grade_period')
        
        ordinary = subject_courses.filter(grade_period__code_name = 'OE')
        extraordinary = subject_courses.filter(grade_period__code_name = 'E')

        if len(extraordinary) > 0:
            last_ordinary = ordinary.last()
            last_extraordinary = extraordinary.last()
            extraordinary_grade, E_is_SD = gradeConverter(last_extraordinary.grade)
            ordinary_grade, OE_is_SD = gradeConverter(last_ordinary.grade)

            if len(ordinary) == len(extraordinary):
                if E_is_SD or extraordinary_grade < 60:
                    risk_courses.append(subject_info)
            else:
                if last_ordinary.school_cycle == last_extraordinary.school_cycle:
                    if E_is_SD or extraordinary_grade < 60:
                        risk_courses.append(subject_info)
                else:
                    if OE_is_SD or ordinary_grade < 60:
                        risk_courses.append(subject_info)
        else:
            last_ordinary = ordinary.last()
            ordinary_grade, OE_is_SD = gradeConverter(last_ordinary.grade)
            if OE_is_SD or ordinary_grade < 60:
                risk_courses.append(subject_info)

    return risk_courses, len(risk_courses)

def predictRisk(student, courses, career, total_credits, remaining_credits, average, semesters):
    model_path = 'IAmodels/IAmodel.pkl'
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    student_vector = getStudentVector(student, courses, career, total_credits, remaining_credits, average, semesters)

    prediction_prob = model.predict_proba(student_vector)
    risk_student_prob = prediction_prob[0][0]

    return risk_student_prob, student_vector


def getStudentVector(student, courses, career, accumulated_credits, missing_credits, average, semesters):
    vectorMaxSubjects = 75   # No. Columns related to subjects

    subject_indexes = courses.values_list('section__subject__idSubject', flat=True).distinct()
    subjects_indexes = list(set(subject_indexes))
    if len(subjects_indexes) > vectorMaxSubjects:
        subjects_indexes = subjects_indexes[:75]

    def statusCheck(student):
        if student.status.code_name in ['AC', 'AI', 'EG', 'ES', 'FI', 'IN', 'GD', 'PP', 'PS', 'PT', 'SS', 'ST', 'TT', 'XI']:
            return 1
        
        return 0
    
    # Fill student info
    data = {
        'status': statusCheck(student),
        'exchange': int(student.exchange),
        'semesters': semesters,
        'accumulated_credits': accumulated_credits,
        'missing_credits': missing_credits,
        'average': average,
    }

    # Fill taken subjects info
    has_practices = False
    i = 0
    for index in subjects_indexes:
        subject_info = Subject.objects.get(idSubject=index)
        subject_coursed = courses.filter(section__subject__idSubject=index).order_by('school_cycle__year', 
                                                                                     'school_cycle__cycle_period',
                                                                                     'grade_period')

        ordinary = subject_coursed.filter(grade_period__code_name = 'OE')
        extraordinary = subject_coursed.filter(grade_period__code_name = 'E')

        if subject_info.name == 'PRACTICAS PROFESIONALES':
            has_practices = True

        if len(extraordinary) > 0 and subject_info.name != 'PRACTICAS PROFESIONALES':
            last_ordinary = ordinary.last()
            last_extraordinary = extraordinary.last()
            extraordinary_grade, E_is_SD = gradeConverter(last_extraordinary.grade)
            ordinary_grade, OE_is_SD = gradeConverter(last_ordinary.grade)

            if len(ordinary) == len(extraordinary):
                if not E_is_SD and extraordinary_grade > 59:
                    data['subject' + str(i)] = len(ordinary)
                else:
                    data['subject' + str(i)] = -1
            else:
                if last_ordinary.school_cycle == last_extraordinary.school_cycle:
                    if not E_is_SD and extraordinary_grade > 59:
                        data['subject' + str(i)] = len(ordinary)
                    else:
                        data['subject' + str(i)] = -1
                else:
                    if not OE_is_SD and ordinary_grade > 59:
                        data['subject' + str(i)] = len(ordinary)
                    else:
                        data['subject' + str(i)] = -1
        else:
            last_ordinary = ordinary.last()
            ordinary_grade, OE_is_SD = gradeConverter(last_ordinary.grade)
            if not OE_is_SD and ordinary_grade > 59:
                data['subject' + str(i)] = len(ordinary)
            else:
                data['subject' + str(i)] = -1
    
        i += 1

    # Finish to fill the columns related to subjects
    while(i < vectorMaxSubjects):
        data['subject' + str(i)] = 0
        i += 1

    # Finish putting if he has practices or not
    data['practices'] = int(has_practices)

    # Converts the dictionary into a dataframe
    df = pd.DataFrame([data])

    # Converts the df into a numpy array
    student_vector = np.array(df.iloc[0])
    student_vector = student_vector[1:]     # Descart prediction variable Y
    student_vector = np.array(student_vector).reshape(1, -1)
        
    return student_vector