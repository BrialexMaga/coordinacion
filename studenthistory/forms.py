from django import forms

class StudentCodeForm(forms.Form):
    student_code = forms.CharField(label='Código', max_length=9)