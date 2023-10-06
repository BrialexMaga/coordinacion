from django import forms
from .models import Student, Contact, School_Cycle

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["code", "name", "status", "admission_cycle"]
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["phone", "email", "udg_email", "emergency_phone", "url_socialnet"]