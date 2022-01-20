from django.contrib import admin

from AppCoderFinal.models import Alojamientos, Destinos, Excursiones

# Register your models here.

admin.site.register(Destinos)
admin.site.register(Alojamientos)
admin.site.register(Excursiones)