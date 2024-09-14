from django import forms
from testapp.models import senrollment_model

class student_form(forms.ModelForm):
    class Meta:
        model=senrollment_model
        fields='__all__'