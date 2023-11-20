from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicio, name='inicio'),
    path('pagina',views.respuesta,name='pagina'),
    path('usuarios',views.usuarios, name="usuarios"),
    path('servicios',views.servicios, name='servicios'),
    path('usuarios/crear',views.crear,name='crear'),
    path('usuarios/editar/<int:id>',views.editar, name='editar'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
    

]