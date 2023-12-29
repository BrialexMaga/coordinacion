from django.shortcuts import render, redirect
from .forms import byCycleForm, byCycleAndSubjectForm, byCycleRangeForm
from studentform.models import Subject

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
            statistics = makeByCycleStatistics(courses)

            return render(request, 'rateSubjectFailures/by_cycle.html', 
                          {'statistics': statistics})

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
    for subject_index in subject_indexes:
        subject = Subject.objects.get(idSubject=subject_index)
        subject_courses = courses.filter(section__subject__idSubject=subject_index).order_by('section__section', 'student__idStudent', 
                                                                                                'grade_period__code_name')

        section_indexes = subject_courses.values_list('section__section', flat=True).distinct()
        
        section_fail_rates = []
        for section_index in section_indexes:
            section_courses = subject_courses.filter(section__section=section_index)

            total_students = section_courses.values_list('student__idStudent', flat=True).distinct().count()
            passed_extraordinary = section_courses.filter(grade_period__code_name='E', grade__gte='59').values_list('student__idStudent', flat=True)

            section_courses_failed_numeric = section_courses.filter(grade__lt='60', grade_period__code_name='OE')
            section_courses_failed_numeric = section_courses_failed_numeric.exclude(student__idStudent__in=passed_extraordinary).count()

            section_courses_failed_sd = section_courses.filter(grade='SD', grade_period__code_name='OE')
            section_courses_failed_sd = section_courses_failed_sd.exclude(student__idStudent__in=passed_extraordinary).count()

            section_courses_failed = section_courses_failed_numeric + section_courses_failed_sd

            failed_rate = section_courses_failed / total_students * 100
            failed_rate = round(failed_rate, 2)

            section_fail_rates.append(failed_rate)

        total_students = subject_courses.values_list('student__idStudent', flat=True).distinct().count()
        passed_extraordinary = subject_courses.filter(grade_period__code_name='E', grade__gte='59').values_list('student__idStudent', flat=True)

        subject_courses_failed_numeric = subject_courses.filter(grade__lt='60', grade_period__code_name='OE')
        subject_courses_failed_numeric = subject_courses_failed_numeric.exclude(student__idStudent__in=passed_extraordinary).count()

        subject_courses_failed_sd = subject_courses.filter(grade='SD', grade_period__code_name='OE')
        subject_courses_failed_sd = subject_courses_failed_sd.exclude(student__idStudent__in=passed_extraordinary).count()

        subject_courses_failed = subject_courses_failed_numeric + subject_courses_failed_sd

        failed_rate = subject_courses_failed / total_students * 100
        failed_rate = round(failed_rate, 2)

        section_fail_rate = sum(section_fail_rates) / len(section_fail_rates) if section_fail_rates else 0
        section_fail_rate = round(section_fail_rate, 2)

        statistics.append({'key_subject': subject.key_subject, 'subject': subject.name, 
                            'section_fail_rate': section_fail_rate, 'total_students': total_students, 
                            'total_failed': subject_courses_failed, 'failed_rate': failed_rate})
    
    return statistics