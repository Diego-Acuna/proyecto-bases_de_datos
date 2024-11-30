from django.urls import path

from . import views

urlpatterns = [

    path('menu_consultas/', views.menu_consultas, name='menu_consultas'),
]