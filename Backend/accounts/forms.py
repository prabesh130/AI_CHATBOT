from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True,
                          widget=forms.EmailInput(attrs={
                                                  'class':'form-input',
                                                  'placeholder':'Email'}))
    username=forms.CharField(required=True,
                          widget=forms.TextInput(attrs={
                                                  'class':'form-input',
                                                  'placeholder':'Username'})
                                                    )
    password=forms.CharField(required=True,
                          widget=forms.TextInput(attrs={
                                                  'class':'form-input',
                                                  'placeholder':'Password'})
                                                    )
    class Meta:
        model=User
        fields={'username','email','password1','password2'}
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email     
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-input',
        'placeholder':'Username'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-input',
        'placeholder':'Password'
    }))
    