from django import forms
class StudentQuery(forms.Form):
    Name=forms.CharField(max_length=30)
    rollno=forms.IntegerField()
    feedback=forms.CharField(max_length=50)