from django import forms
from testapp.models import employee_model,blog_model

class blog_form(forms.ModelForm):
    class Meta:
        model=blog_model
        field='__all__'

