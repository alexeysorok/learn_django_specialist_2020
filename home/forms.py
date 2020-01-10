from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(label='password')

