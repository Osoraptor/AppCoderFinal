from django.urls import path
from AppCoderFinal import views

urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('destinos/', views.destinos, name="destinos"),
    path('alojamientos/', views.alojamientos, name="alojamientos"),
    path('excursiones/', views.excursiones, name="excursiones"),
    path('destinoForm/', views.destinoForm, name="DestinoFormulario"),
    path('alojamientoForm/', views.alojamientoForm, name="AlojamientoFormulario"),
    path('excursionForm/', views.excursionForm, name="ExcursionFormulario"),
    path('busquedaDestino/', views.busquedaDestino, name="BusquedaDestino"),
    path('buscarDestino/', views.buscarDestino, name="BuscarDestino"),
]

