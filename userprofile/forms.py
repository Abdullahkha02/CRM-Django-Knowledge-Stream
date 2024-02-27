from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':' Your UserName',
        'class':'w-full my-4 py-4 py-6 rounded-xl bg-gray-100'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' :' Your Password',
        'class' : 'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your UserName',
        'class':'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your Email Adress',
        'class':'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your Password',
        'class':'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat Password',
        'class':'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'
    }))