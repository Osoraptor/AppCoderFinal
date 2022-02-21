from django.contrib import admin

from AppCoderFinal.models import Alojamientos, Avatar, Destinos, Excursiones

# Register your models here.

admin.site.register(Destinos)
admin.site.register(Alojamientos)
admin.site.register(Excursiones)
admin.site.register(Avatar)