from django import forms
from testapp.models import student_model

class Student_Form(forms.ModelForm):
    class meta:
        model=student_model
        field='__all__'