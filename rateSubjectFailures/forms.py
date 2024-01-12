from django import forms
from studenthistory.models import Course
from studentform.models import School_Cycle, Subject
from django.db.models import Q

class byCycleForm(forms.Form):
    school_cycle = forms.ModelChoiceField(
        label='',
        queryset=School_Cycle.objects.all().order_by('-year', '-cycle_period'), 
        empty_label="----Ciclo----"
        )

    def filter_courses(self):
        school_cycle = self.cleaned_data.get('school_cycle')
        courses = Course.objects.all()

        if school_cycle:
            courses = courses.filter(school_cycle=school_cycle)

        return courses

class byCycleAndSubjectForm(forms.Form):
    school_cycle = forms.ModelChoiceField(
        label='',
        queryset=School_Cycle.objects.all().order_by('-year', '-cycle_period'), 
        empty_label="----Ciclo----"
        )
    subject = forms.ModelChoiceField(
        label='',
        queryset=Subject.objects.all().order_by('key_subject'),
        empty_label="----Materia----"
        )

    def filter_courses(self):
        school_cycle = self.cleaned_data.get('school_cycle')
        subject = self.cleaned_data.get('subject')

        courses = Course.objects.all()

        if school_cycle:
            courses = courses.filter(school_cycle=school_cycle)

        if subject:
            courses = courses.filter(section__subject=subject)

        return courses

class byCycleRangeForm(forms.Form):
    start_cycle = forms.ModelChoiceField(
        label='Desde:',
        queryset=School_Cycle.objects.all().order_by('year', 'cycle_period'),
        empty_label="----Ciclo----"
        )
    end_cycle = forms.ModelChoiceField(
        label='Hasta:',
        queryset=School_Cycle.objects.all().order_by('-year', '-cycle_period'),
        empty_label="----Ciclo----"
        )

    def filter_courses(self):
        start_cycle = self.cleaned_data.get('start_cycle')
        end_cycle = self.cleaned_data.get('end_cycle')

        courses = Course.objects.all()

        if start_cycle and end_cycle:
            courses = courses.filter(
                Q(school_cycle__year__gt=start_cycle.year) |
                Q(school_cycle__year=start_cycle.year, school_cycle__cycle_period__gte=start_cycle.cycle_period),
                Q(school_cycle__year__lt=end_cycle.year) |
                Q(school_cycle__year=end_cycle.year, school_cycle__cycle_period__lte=end_cycle.cycle_period)
            )

        return courses