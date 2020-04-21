from django.urls import path
from bdHakimaru.views import  Home, nueva_pelea, consultar_peleas, consultar_demonios, nuevo_monstruo, nuevo_lugar, objeto_list, nuevo_objeto, borrar_objeto,imprimir_monstruos


urlpatterns = [
    path('',Home.as_view(),name='Home'),
    path('bdHakimaru/new', nueva_pelea.as_view(), name = 'nueva_pelea'),
    path('bdHakimaru/', consultar_demonios.as_view(),name = 'consultar_demonios'),
    path('bdHakimaru/peleas', consultar_peleas.as_view(),name = 'consultar_peleas'),
    path('bdHakimaru/new_monster',nuevo_monstruo.as_view(),name = 'nuevo_monstruo'),
    path('bdHakimaru/new_place',nuevo_lugar.as_view(), name = 'nuevo_lugar'),
    path('bdHakimaru/objeto_list',objeto_list.as_view(), name = 'objetos_dororo'),
    path('bdHakimaru/nuevo_objeto',nuevo_objeto.as_view(), name = 'nuevo_objeto'),
    path('bdHakimaru/delete/<int:pk>',borrar_objeto.as_view(), name = 'borrar_objeto'),
    path('bdHakimaru/imprimir',imprimir_monstruos,name = 'imprimir_monstruos'),
]