from django.shortcuts import render, redirect
from django.db import transaction

from .models import Student, Contact, School_Cycle
from .forms import StudentForm
from .factories import StudentFactory

# Create your views here.
from django.http import HttpResponse

def index(request):
    students = Student.objects.all()
    contacts = Contact.objects.all()
    cycles = School_Cycle.objects.all()
    return render(request, "studentform/index.html", {'students':students, 'contacts':contacts, 'cycles':cycles})

def createFormStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Saves Form in the DataBase
            '''
            code = form.cleaned_data['code']
            name = form.cleaned_data['name']
            status = form.cleaned_data['status']

            student = Student(code=code, name=name, status=status)
            student.save()
            '''

            # Factory
            callStudentFactory()

            return redirect('index') # Put the name of the views in here to redirect.
    else:
        form = StudentForm()
    
    return render(request, "studentform/student_form.html", {'form': form})

@transaction.atomic
def callStudentFactory():
    # Factory
    students = StudentFactory.create_batch(13)

    for student in students:
        student.save()