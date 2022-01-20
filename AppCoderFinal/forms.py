from django import forms

class AlojamientosForm(forms.Form):

    tipo = forms.CharField()
    precio = forms.FloatField()
    visitantes = forms.IntegerField()


class ExcursionesForm(forms.Form):

    lugar = forms.CharField()
    duracion = forms.IntegerField()
    precio = forms.FloatField()