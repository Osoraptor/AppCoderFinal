from django.shortcuts import render
from AppCoderFinal.forms import AlojamientosForm, DestinosForm, ExcursionesForm

from AppCoderFinal.models import Alojamientos, Destinos, Excursiones
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

### Para el LOGIN ###

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(req):

    return render(req, 'AppCoderFinal/inicio.html')

def destinos(req):

    lista = Destinos.objects.all()

    return render(req, 'AppCoderFinal/destinos.html', {"lista": lista})

@login_required
def alojamientos(req):

    lista = Alojamientos.objects.all()
    
    return render(req, 'AppCoderFinal/alojamientos.html', {"lista": lista})

@login_required
def excursiones(req):

    lista = Excursiones.objects.all()
    
    return render(req, 'AppCoderFinal/excursiones.html', {"lista": lista})


###### FORMULARIOS POST ##########

### DESTINO FORM ###

def destinoForm(request):

    #print(request.POST) ### Nota: Validar lo que viene en el POST. ###

    if(request.method == 'POST'):

        miForm = DestinosForm(request.POST)

        if(miForm.is_valid()):

            data = miForm.cleaned_data

            destino = Destinos(pais=request.POST["pais"], ciudad=request.POST["ciudad"])
            
            destino.save()

            return render(request, "AppCoderFinal/inicio.html")
    
    else:

        miForm = DestinosForm()

    return render(request, "AppCoderFinal/destinoForm.html", {'miForm': miForm})


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


###### FORMULARIOS CRUD ##########

    ### READ ###

def leerDestinos(request):
    
    destinos = Destinos.objects.all()

    return render(request, "AppCoderFinal/leerDestinos.html", {"destinos": destinos} )

    ### CREATE ###

    # Nota Esto ya esta hecho con los forms los cuales vienen siendo el CREATE del CRUD #

    ### DELETE ###

def delDestino(request, id_destino):

    destino = Destinos.objects.get(id=id_destino)

    destino.delete()

    return render(request, "AppCoderFinal/leerDestinos.html", {"destinos": destinos} )

    ### EDIT ###

def editDestino(request, id_destino):

    #Recibe el ID del destino que se va a modificar
    destino = Destinos.objects.get(id=id_destino)

    #Si es metodo POST se hace lo mismo que el CREATE
    if(request.method == 'POST'):

        miForm = DestinosForm(request.POST)

        print(miForm)

        if(miForm.is_valid()): ### Validacion de Django

            data = miForm.cleaned_data

            destino.pais = data['pais']
            destino.ciudad = data['ciudad']

            destino.save()

            return render(request, "AppCoderFinal/inicio.html") # Volver a inicio

    else:

        miForm= DestinosForm(initial={'pais': destino.pais, 'ciudad': destino.ciudad})

    return render(request, "AppCoderFinal/editarDestino.html", {"miForm": miForm, "id_destino": id_destino})
    
####################################################

    ### CLASES BASADAS EN VISTAS ###

        ### DESTINOS ###


class DestinosList(LoginRequiredMixin ,ListView):

    model = Destinos
    template_name = "AppCoderFinal/destinos_list.html"

class DestinoDetail(LoginRequiredMixin ,DetailView):

    model = Destinos
    template_name = "AppCoderFinal/destino_detalle.html"

class DestinoCreate(LoginRequiredMixin ,CreateView): #DONE

    model = Destinos
    success_url = "/AppCoderFinal/listaDestinos"
    fields = ['pais', 'ciudad']   
    template_name = "AppCoderFinal/destino_create.html" 

class DestinoUpdate(LoginRequiredMixin ,UpdateView): #DONE

    model = Destinos
    fields = ['pais', 'ciudad'] 
    success_url = "/AppCoderFinal/listaDestinos"
    template_name = "AppCoderFinal/destino_form.html"   

class DestinoDelete(LoginRequiredMixin ,DeleteView): #PENDING

    model = Destinos
    success_url = "/AppCoderFinal/listaDestinos"


##################################################

    ### LOGIN ####

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)


            if user is not None:
                login(request, user)

                return render(request, "AppCoderFinal/inicio.html", {"mensaje":f"Bienvenido {usuario}"} )
            
            else:

                return render(request, "AppCoderFinal/inicio.html", {"mensaje":"Error, datos incorrectos."} )
        
        else:

            return render(request, "AppCoderFinal/inicio.html", {"mensaje":"Error, formulario erroneo."} )

    else:
        
        form = AuthenticationForm()

        return render(request, "AppCoderFinal/login.html", {'form':form} )


    ### REGISTRO ####

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoderFinal/inicio.html", {"mensaje":"Usuario Creado :)"} )

        else:

            return render(request, "AppCoderFinal/inicio.html", {"mensaje":"Usuario NO creado!"} )

    
    else:
        
        form = UserCreationForm()

        return render(request, "AppCoderFinal/registro.html", {'form':form} )



