from django import forms

class ReaderAccessForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(required=True)

class LoginForm(forms.Form):
    email = forms.EmailField(label="Enter your Email to Login")
