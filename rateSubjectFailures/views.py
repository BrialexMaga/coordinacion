from django.shortcuts import render, redirect
from .forms import byCycleForm, byCycleAndSubjectForm, byCycleRangeForm
from studentform.models import Subject
from studenthistory.models import Section

def filterRateSubjectFailures(request):
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
            statistics, registers = makeByCycleStatistics(courses)

            return render(request, 'rateSubjectFailures/by_cycle.html', 
                          {'statistics': statistics, 'registers': registers})

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






def makeByCycleStatistics(courses):
    subject_indexes = courses.values_list('section__subject__idSubject', flat=True).distinct()

    statistics = []
    registers = []
    for subject_index in subject_indexes:
        subject = Subject.objects.get(idSubject=subject_index)
        subject_courses = courses.filter(section__subject__idSubject=subject_index).order_by('section__section', 'student__idStudent', 
                                                                                                'grade_period__code_name')

        section_indexes = subject_courses.values_list('section__idSection', flat=True).distinct()
        section_indexes = list(set(section_indexes))
        
        section_fail_rates = []
        for section_index in section_indexes:
            calculatePercent = lambda x, y: round(x / y * 100, 2) if y else 0
            section_courses = subject_courses.filter(section__idSection=section_index)
            section = Section.objects.get(idSection=section_index)

            total_students = section_courses.values_list('student__idStudent', flat=True).distinct().count()
            passed_extraordinary = section_courses.filter(grade_period__code_name='E', grade__gte='60').values_list('student__idStudent', flat=True).distinct()
            another_passed_extraordinary = subject_courses.filter(grade_period__code_name='OE', grade__gte='100').values_list('student__idStudent', flat=True)
            passed_extraordinary = list(set(passed_extraordinary) | set(another_passed_extraordinary))
            
            no_passed_extraordinary = len(passed_extraordinary)
            no_passed_ordinary = section_courses.filter(grade_period__code_name='OE', grade__gte='60').count()
            no_failed_extraordinary = section_courses.filter(grade_period__code_name='E', grade__lt='60').count()
            no_failed_extraordinary += section_courses.filter(grade_period__code_name='E', grade='SD').count()

            section_courses_failed_numeric = section_courses.filter(grade_period__code_name='OE', grade__lt='60')
            no_failed_ordinary = section_courses_failed_numeric.count()
            section_courses_failed_numeric = section_courses_failed_numeric.exclude(student__idStudent__in=passed_extraordinary).count()

            section_courses_failed_sd = section_courses.filter(grade_period__code_name='OE', grade='SD')
            no_sd_ordinary = section_courses_failed_sd.count()
            no_failed_ordinary += no_sd_ordinary
            section_courses_failed_sd = section_courses_failed_sd.exclude(student__idStudent__in=passed_extraordinary).count()

            section_courses_failed = section_courses_failed_numeric + section_courses_failed_sd

            no_sd = no_sd_ordinary #+ section_courses.filter(grade_period__code_name='E', grade='SD').count()

            SD_percent = calculatePercent(no_sd, total_students)
            OE_percent = calculatePercent(no_passed_ordinary, total_students)
            E_percent = calculatePercent(no_passed_extraordinary, total_students)
            NO_OE_percent = calculatePercent(no_failed_ordinary, total_students)
            NO_E_percent = calculatePercent(no_failed_extraordinary, total_students)

            failed_rate = section_courses_failed / total_students * 100
            failed_rate = round(failed_rate, 2)

            section_fail_rates.append(failed_rate)
            registers.append({'key_subject': subject.key_subject, 'subject': subject.name, 'section': section.section, 'total_students': total_students,
                              'SD': no_sd, 'OE': no_passed_ordinary, 'E': no_passed_extraordinary, 'NO_OE': no_failed_ordinary,
                              'NO_E': no_failed_extraordinary, 'SD_percent': SD_percent, 'OE_percent': OE_percent, 'E_percent': E_percent,
                              'NO_OE_percent': NO_OE_percent, 'NO_E_percent': NO_E_percent})

        total_students = subject_courses.values_list('student__idStudent', flat=True).distinct().count()
        passed_extraordinary = subject_courses.filter(grade_period__code_name='E', grade__gte='60').values_list('student__idStudent', flat=True)
        another_passed_extraordinary = subject_courses.filter(grade_period__code_name='OE', grade__gte='100').values_list('student__idStudent', flat=True)
        passed_extraordinary = list(set(passed_extraordinary) | set(another_passed_extraordinary))

        subject_courses_failed_numeric = subject_courses.filter(grade_period__code_name='OE', grade__lt='60')
        subject_courses_failed_numeric = subject_courses_failed_numeric.exclude(student__idStudent__in=passed_extraordinary).count()

        subject_courses_failed_sd = subject_courses.filter(grade_period__code_name='OE', grade='SD')
        subject_courses_failed_sd = subject_courses_failed_sd.exclude(student__idStudent__in=passed_extraordinary).count()

        subject_courses_failed = subject_courses_failed_numeric + subject_courses_failed_sd

        failed_rate = subject_courses_failed / total_students * 100
        failed_rate = round(failed_rate, 2)

        section_fail_rate = sum(section_fail_rates) / len(section_fail_rates) if section_fail_rates else 0
        section_fail_rate = round(section_fail_rate, 2)

        statistics.append({'key_subject': subject.key_subject, 'subject': subject.name, 
                            'section_fail_rate': section_fail_rate, 'total_students': total_students, 
                            'total_failed': subject_courses_failed, 'failed_rate': failed_rate})
    
    return statistics, registers