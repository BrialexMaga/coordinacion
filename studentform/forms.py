from django import forms
from .models import Student, Contact, School_Cycle

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["code", "name", "status", "admission_cycle"]
        labels = {
            "code": "Código",
            "name": "Nombre",
            "status": "Estatus",
            "admission_cycle": "Ciclo de Admisión"
        }
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["phone", "email", "udg_email", "emergency_phone", "url_socialnet",
                  "company", "position"]
        labels = {
            "phone": "Teléfono",
            "email": "Correo Electronico", 
            "udg_email": "Correo de UDG", 
            "emergency_phone": "Teléfono de Emergencia", 
            "url_socialnet": "URL de Red Social",
            "company": "Compañia donde trabaja", 
            "position": "Posición"
        }