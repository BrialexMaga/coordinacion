from django.contrib import admin
from .models import Student, Contact, School_Cycle, Career, Status

admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(School_Cycle)
admin.site.register(Career)
admin.site.register(Status)