from django import forms
from testapp.models import blog

class BlogForm(forms.ModelForm):
    class Meta:
        model=blog
        fields='__all__'