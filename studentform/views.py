from django.shortcuts import render
from .models import Student, Contact, School_Cycle
# Create your views here.
from django.http import HttpResponse

def index(request):
    students = Student.objects.all()
    contacts = Contact.objects.all()
    cycles = School_Cycle.objects.all()
    return render(request, "studentform/index.html", {'students':students, 'contacts':contacts, 'cycles':cycles})