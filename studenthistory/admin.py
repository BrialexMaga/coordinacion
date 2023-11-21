from django.contrib import admin
from .models import Subject, Section, GradePeriod, Course, CareerSubject

admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(GradePeriod)
admin.site.register(Course)
admin.site.register(CareerSubject)