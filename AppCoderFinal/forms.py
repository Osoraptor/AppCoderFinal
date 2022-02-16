from django import forms

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

