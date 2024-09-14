from django import forms

class signup(forms.Form):
    name=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
    rpassword=forms.CharField(max_length=30)

    def clean(self):
        total_cleaned_data=super().clean()
        passw=total_cleaned_data['password']
        print(passw,'hit')
        rpass=total_cleaned_data['rpassword']
        print(passw,'hit')
        if passw != rpass:
            raise forms.ValidationError('password not matched')