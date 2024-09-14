from django import forms

class blog_form(forms.Form):
    title=forms.CharField()
    about=forms.CharField(widget=forms.Textarea)