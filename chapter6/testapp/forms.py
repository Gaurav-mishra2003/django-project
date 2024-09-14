from django import forms
from .models import signup

class signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'


        
    def clean(self):
       total_cleaned=  super().clean()
       password=total_cleaned['password']
       rpassword=total_cleaned['rpassword']
       if password !=rpassword:
           raise forms.ValidationError('value not mached')
       