from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """
    TODO: em modo de produção alterar as variávies de:

    psk/psk/settings.py

    LOGIN_URL = '/entrar/'
    LOGIN_REDIRECT_URL = '/'
    LOGOUT_REDIRECT_URL = '/'
    
    para o local exato em que se encontrará o profile do cliente.    
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Seu nome de usuário",
        'class': "w-full py-4 px-6 rounded-xl",        
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Sua senha",
        'class': "w-full py-4 px-6 rounded-xl",        
    }))



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Seu nome de usuário",
        'class': "w-full py-4 px-6 rounded-xl",        
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Seu E-mail",
        'class': "w-full py-4 px-6 rounded-xl",        
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Sua senha",
        'class': "w-full py-4 px-6 rounded-xl",        
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Repita sua senha",
        'class': "w-full py-4 px-6 rounded-xl",        
    }))