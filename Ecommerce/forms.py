from django import forms
from .models import Person
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    first_name = forms.CharField(widget=forms.TextInput, label="Nom")
    last_name = forms.CharField(widget=forms.TextInput, label="Prenom")
    
    def clean(self):

        cleaned_data = self.cleaned_data
        password_1 = cleaned_data.get("password")
        password_2 = cleaned_data.get("password2")
        user_email = cleaned_data.get("email")

        if password_1 != password_2:
            raise ValidationError("Mots de passe differents")
        else:
            if len(password_1) < 8:
                raise ValidationError("Mot de passe trop court, 8 caracteres au minimum")
        email_used = len(Person.objects.filter(email=user_email)) > 0
        if email_used:
            raise ValidationError("Adresse mail déjà utilisée")

    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email", "password", "password2", "phone"]


class LoginForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    def clean(self):
        pass

    class Meta:
        model = Person
        fields = ["email", "password"]
