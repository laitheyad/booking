from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('UserName', 'Password', 'Email',
                'PhoneNumber', 'Acception')

        widgets ={
            'UserName': forms.TextInput(attrs={'class': 'form-control','id':'username', 'placeholder': 'Username'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control','id':'password', 'placeholder': 'Password'}),
            'Email': forms.TextInput(attrs={'class': 'form-control','id':'email', 'placeholder': 'E-mail'}),
            'PhoneNumber': forms.TextInput(attrs={'class': 'form-control','id':'phone', 'placeholder': 'Phone'}),
            'Acception': forms.CheckboxInput(attrs={'class': 'form-check-input','id':'sure'}),
            }