from django.urls import path
from AppCoderFinal import views

from django.contrib.auth.views import LogoutView

urlpatterns = [

    ### URLS MODULOS ####
    path('', views.inicio, name="inicio"),
    path('destinos/', views.destinos, name="destinos"),
    path('alojamientos/', views.alojamientos, name="alojamientos"),
    path('excursiones/', views.excursiones, name="excursiones"),
    
    ### URLS FORMS ####
    path('destinoForm/', views.destinoForm, name="DestinoFormulario"),
    path('alojamientoForm/', views.alojamientoForm, name="AlojamientoFormulario"),
    path('excursionForm/', views.excursionForm, name="ExcursionFormulario"),
    path('busquedaDestino/', views.busquedaDestino, name="BusquedaDestino"),
    path('buscarDestino/', views.buscarDestino, name="BuscarDestino"),

    ### URLS CRUDS ####

    path('leerDestinos/', views.leerDestinos, name="LeerDestinos"),
    path('borrarDestino/<id_destino>/', views.delDestino, name="BorrarDestino"),
    path('editDestino/<id_destino>/', views.editDestino, name="EditarDestino"),


     ### URLS CBV ####
        ##DESTINOS###

    path('listaDestinos/', views.DestinosList.as_view(), name="List"),
    path('detalleDestino/<pk>/', views.DestinoDetail.as_view(), name="Detail"),
    path('crearDestino/', views.DestinoCreate.as_view(), name="Create"),
    path('editarDestino/<pk>/', views.DestinoUpdate.as_view(), name="Update"),
    path('eliminarDestino/<pk>/', views.DestinoDelete.as_view(), name="Delete"),
    
    ### LOGIN ###

    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Registro"),
    path('logout/', LogoutView.as_view(template_name='AppCoderFinal/logout.html'), name="Logout"),
     path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),

]

