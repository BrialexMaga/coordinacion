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
    url_socialnet = forms.CharField(required=False)

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
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['phone'].required = True
        self.fields['email'].required = True
        self.fields['udg_email'].required = True
        self.fields['emergency_phone'].required = True
    
    def clean_url_socialnet(self):
        url = self.cleaned_data.get('url_socialnet')
        if url and not url.startswith(('http://', 'https://')):
            url = f'http://{url}'
        
        return url