from django import forms

class student_form(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()
    rollno=forms.IntegerField()