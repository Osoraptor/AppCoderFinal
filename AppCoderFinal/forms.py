from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DestinosForm(forms.Form):

    pais = forms.CharField()
    ciudad = forms.CharField()


class AlojamientosForm(forms.Form):

    tipo = forms.CharField()
    precio = forms.FloatField()
    visitantes = forms.IntegerField()


class ExcursionesForm(forms.Form):

    lugar = forms.CharField()
    duracion = forms.IntegerField()
    precio = forms.FloatField()



### EDITAR PERFIL ###

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ]


### REGISTRO ###

# class UserRegisterForm(UserCreationForm):

#     email = forms.EmailField()
#     password1 = forms.Charfield(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.Charfield(label='Repetir la contraseña', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'password2']
#         #Saco los mensajes de ayuda
#         help_texts = {k:"" for k in fields}

