from testapp.models import blog_model,student_attendence,student_enrollment
from django import forms
from django.contrib.auth.models import User 

class blog_form(forms.ModelForm):
    class Meta:
        model=blog_model
        fields='__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class Sattedence_form(forms.ModelForm):
    class Meta:
        model=student_attendence
        fields='__all__'

class Senrollment_form(forms.ModelForm):
    class Meta:
        model=student_enrollment
        fields='__all__'

  