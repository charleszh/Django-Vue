from django import forms
from django.contrib.auth.models import User
import re

def checkEmail(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+\"?)")
    return re.match(pattern, email)

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6:
            raise forms.ValidationError("Your username must be at least 6 characters long")
        elif len(username) > 50:
            raise forms.ValidationError("Your username must be no more than 50 characters long")
        else:
            filterResult = User.objects.filter(username__exact=username)
            if len(filterResult) > 0:
                raise forms.ValidationError("Your username is already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if checkEmail(email):
            filterResult = User.objects.filter(email__exact=email)
            if len(filterResult) > 0:
                raise forms.ValidationError("Your email is already exists")
        else:
            raise forms.ValidationError("Please enter a valid email")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("Your password must be at least 6 characters long")
        elif len(password) > 20:
            raise forms.ValidationError("Your password must be no more than 20 characters long")

        return password

    def clean_confirm_password(self):
        confirmPassword = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if password and confirmPassword and password != confirmPassword:
            raise forms.ValidationError("Password mismatch")

        return confirmPassword

class LoginForm(forms.Form):

    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if checkEmail(username):
            filterResult = User.objects.filter(emaial__exact=username)
            if not filterResult:
                raise forms.ValidationError("This email does not exist")
        else:
            filterResult = User.objects.filter(username__exact=username)
            if not filterResult:
                raise forms.ValidationError("This username does not exist. Please register a new one")

        return username

