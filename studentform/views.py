from django.shortcuts import render
from .models import Student, Contact, School_Cycle
from .forms import StudentForm
# Create your views here.
from django.http import HttpResponse

def index(request):
    students = Student.objects.all()
    contacts = Contact.objects.all()
    cycles = School_Cycle.objects.all()
    return render(request, "studentform/index.html", {'students':students, 'contacts':contacts, 'cycles':cycles})

#Checar esta funcion, ya que el formulario no crea un nuevo estudiante.
def createFormStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            name = form.cleaned_data['name']
            status = form.cleaned_data['status']

            # Save
            student = Student(code=code, name=name, status=status)
            student.save()
    else:
        form = StudentForm()
    
    return render(request, "studentform/student_form.html", {'form': form})