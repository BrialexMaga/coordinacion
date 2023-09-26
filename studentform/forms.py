from django import forms

class StudentForm(forms.Form):
    code = forms.CharField(max_length=9, label='Código')
    name = forms.CharField(max_length=100, label='Nombre')
    status = forms.CharField(max_length=10, label='Estatus')
    