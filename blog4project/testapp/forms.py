from django import forms

class blog_form(forms.Form):
    title=forms.CharField(max_length=50)
    description=forms.CharField(max_length=200)