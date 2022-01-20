from django.shortcuts import render
from AppCoderFinal.forms import AlojamientosForm, ExcursionesForm

from AppCoderFinal.models import Alojamientos, Destinos, Excursiones
from django.http import HttpResponse


# Create your views here.

def inicio(req):

    return render(req, 'AppCoderFinal/inicio.html')

def destinos(req):

    lista = Destinos.objects.all()

    return render(req, 'AppCoderFinal/destinos.html', {"lista": lista})

def alojamientos(req):

    lista = Alojamientos.objects.all()
    
    return render(req, 'AppCoderFinal/alojamientos.html', {"lista": lista})

def excursiones(req):

    lista = Excursiones.objects.all()
    
    return render(req, 'AppCoderFinal/excursiones.html', {"lista": lista})


###### FORMULARIOS POST ##########

### DESTINO FORM ###

def destinoForm(request):

    #print(request.POST) ### Nota: Validar lo que viene en el POST. ###

    if(request.method == 'POST'):

        destino = Destinos(pais=request.POST["pais"], ciudad=request.POST["ciudad"])
        destino.save()

        return render(request, "AppCoderFinal/inicio.html")

    
    return render(request, "AppCoderFinal/destinoForm.html")


### ALOJAMIENTO FORM ###

def alojamientoForm(request):

    #print(request.POST) ### Nota: Validar lo que viene en el POST. ###

    if(request.method == 'POST'):

        miForm = AlojamientosForm(request.POST)

        if(miForm.is_valid()):

            data = miForm.cleaned_data

            alojamiento = Alojamientos(tipo=request.POST["tipo"], precio=request.POST["precio"], visitantes=request.POST["visitantes"])
            
            alojamiento.save()

            return render(request, "AppCoderFinal/inicio.html")
    
    else:

        miForm = AlojamientosForm()

    return render(request, "AppCoderFinal/alojamientoForm.html", {'miForm': miForm})


### EXCURSIONES FORM ###

def excursionForm(request):

    #print(request.POST) ### Nota: Validar lo que viene en el POST. ###

    if(request.method == 'POST'):

        miForm = ExcursionesForm(request.POST)

        if(miForm.is_valid()):

            data = miForm.cleaned_data

            excursion = Excursiones(lugar=request.POST["lugar"], duracion=request.POST["duracion"], precio=request.POST["precio"])
            
            excursion.save()

            return render(request, "AppCoderFinal/inicio.html")
    
    else:

        miForm = ExcursionesForm()

    return render(request, "AppCoderFinal/excursionForm.html", {'miForm': miForm})


###### FORMULARIOS GeT ##########

### DESTINO GET FORM ###

def busquedaDestino(request):

    return render(request, 'AppCoderFinal/busquedaDestino.html')

def buscarDestino(request):

    if(request.method == 'GET'):

        pais = request.GET["pais"]
        ciudades = Destinos.objects.filter(pais=pais)

        return render(request, "AppCoderFinal/resultadosBusqueda.html", {'ciudades': ciudades, 'pais': pais})
    
    else:

        return HttpResponse('No enviaste datos')




    #return render(request, 'AppCoderFinal/busquedaDestino.html')