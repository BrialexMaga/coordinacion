from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction

from .models import Student, Contact, School_Cycle, Career, Status
from .forms import StudentForm, ContactForm
from .factories import StudentFactory

# Create your views here.
from django.http import HttpResponse
import csv

def index(request):
    students = Student.objects.all()
    contacts = Contact.objects.all()
    cycles = School_Cycle.objects.all()
    careers = Career.objects.all()
    statuses = Status.objects.all()

    if request.GET.get('name') or request.GET.get('code'):
        name = request.GET.get('name', '')
        code = request.GET.get('code', '')

        students = students.filter(name__icontains=name, code__icontains=code)

    return render(request, "studentform/index.html", {'students':students, 'contacts':contacts, 
                                                      'cycles':cycles, 'careers':careers, 'statuses':statuses})

def exportContacts(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

    writer = csv.writer(response)
    # Headers
    writer.writerow(['Name', 
                     'Given Name', 'Additional Name', 'Family Name', 
                     'Yomi Name', 'Given Name Yomi', 'Additional Name Yomi', 'Family Name Yomi', 'Name Prefix', 
                     'Name Suffix', 'Initials', 'Nickname', 'Short Name', 'Maiden Name', 
                     'Birthday', 'Gender Location', 'Billing Information Directory Server',	'Mileage Occupation', 'Hobby', 
                     'Sensitivity',	'Priority', 'Subject',	'Notes', 'Language', 'Photo',
                     'Group Membership', 'E-mail 1 - Type', 'E-mail 1 - Value', 'E-mail 2 - Type', 'E-mail 2 - Value',
                     'Phone 1 - Type', 'Phone 1 - Value', 'Phone 2 - Type', 'Phone 2 - Value', 'Organization 1 - Type', 
                     'Organization 1 - Name', 'Organization 1 - Yomi Name', 'Organization 1 - Title', 'Organization 1 - Department', 'Organization 1 - Symbol',
                     'Organization 1 - Location', 'Organization 1 - Job Description', 'Website 1 - Type', 'Website 1 - Value', 'Custom Field 1 - Type', 
                     'Custom Field 1 - Value', 'Custom Field 2 - Type', 'Custom Field 2 - Value'])

    contacts = Contact.objects.all()

    for contact in contacts:
        # Data
        writer.writerow([f'{contact.idStudent.name} {contact.idStudent.first_last_name} {contact.idStudent.second_last_name}', 
                         contact.idStudent.name, "", f'{contact.idStudent.first_last_name} {contact.idStudent.second_last_name}', 
                         "", "", "", "", "",
                         "", "", "", "", "",
                         "", "", "", "", "",
                         "", "", "", "", "", "",
                         "", "Personal", contact.email, "UDG", contact.udg_email, 
                         "Emergencia", contact.emergency_phone, "Personal", contact.phone,  "", 
                         contact.company, "", contact.position, "", "",
                         "", "", "Red Social", contact.url_socialnet, "Codigo Escolar", 
                         contact.idStudent.code, "Estatus", contact.idStudent.status.status])

    return response

def exportStudentData(request, idStudent):
    student = Student.objects.get(pk=idStudent)
    contact = Contact.objects.get(idStudent=student)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{student.name}_{student.first_last_name}_{student.second_last_name}_contact.csv"'

    writer = csv.writer(response)
    # Headers
    writer.writerow(['Name', 
                     'Given Name', 'Additional Name', 'Family Name', 
                     'Yomi Name', 'Given Name Yomi', 'Additional Name Yomi', 'Family Name Yomi', 'Name Prefix', 
                     'Name Suffix', 'Initials', 'Nickname', 'Short Name', 'Maiden Name', 
                     'Birthday', 'Gender Location', 'Billing Information Directory Server',	'Mileage Occupation', 'Hobby', 
                     'Sensitivity',	'Priority', 'Subject',	'Notes', 'Language', 'Photo',
                     'Group Membership', 'E-mail 1 - Type', 'E-mail 1 - Value', 'E-mail 2 - Type', 'E-mail 2 - Value',
                     'Phone 1 - Type', 'Phone 1 - Value', 'Phone 2 - Type', 'Phone 2 - Value', 'Organization 1 - Type', 
                     'Organization 1 - Name', 'Organization 1 - Yomi Name', 'Organization 1 - Title', 'Organization 1 - Department', 'Organization 1 - Symbol',
                     'Organization 1 - Location', 'Organization 1 - Job Description', 'Website 1 - Type', 'Website 1 - Value', 'Custom Field 1 - Type', 
                     'Custom Field 1 - Value', 'Custom Field 2 - Type', 'Custom Field 2 - Value'])
    
    # Data
    writer.writerow([f'{contact.idStudent.name} {contact.idStudent.first_last_name} {contact.idStudent.second_last_name}', 
                    contact.idStudent.name, "", f'{contact.idStudent.first_last_name} {contact.idStudent.second_last_name}', 
                    "", "", "", "", "",
                    "", "", "", "", "",
                    "", "", "", "", "",
                    "", "", "", "", "", "",
                    "", "Personal", contact.email, "UDG", contact.udg_email, 
                    "Emergencia", contact.emergency_phone, "Personal", contact.phone,  "", 
                    contact.company, "", contact.position, "", "",
                    "", "", "Red Social", contact.url_socialnet, "Codigo Escolar", 
                    contact.idStudent.code, "Estatus", contact.idStudent.status.status])
    return response

def showContact(request, idStudent):
    student = get_object_or_404(Student, pk=idStudent)
    contact = student.contact

    return render(request, 'studentform/student_contact.html', {'student': student, 'contact': contact})

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

def createFormContact(request, idStudent):
    student = get_object_or_404(Student, pk=idStudent)
    contact, created = Contact.objects.get_or_create(idStudent=student)

    if request.method == 'POST':
        form = ContactForm(request.POST or None, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm(instance=contact)

    return render(request, "studentform/contact_form.html", {'form': form, 'student': student})

@transaction.atomic
def callStudentFactory():
    # Factory
    students = StudentFactory.create_batch(20)

    for student in students:
        student.save()