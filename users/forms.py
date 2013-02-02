from django import forms
import models

class CreateUserForm(forms.Form):
    nick = forms.CharField(label='nick')
    
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='type your password once more', widget=forms.PasswordInput)
    
    firstname = forms.CharField(label='first name')
    lastname = forms.CharField(label='last name', required=False)
    
    sex = forms.ChoiceField(label='sex', choices=models.UserProfile.SEX_CHOICES)
    
    email = forms.EmailField(label='e-mail')
    
    