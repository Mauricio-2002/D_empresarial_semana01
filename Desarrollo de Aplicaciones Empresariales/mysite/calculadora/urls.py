from django.urls import path

from . import views

urlpatterns =[
    # ex: localhost:8000/calculadora/
    path('',views.index, name='index'),
    # ex: localhost:8000/calculadora/18/19/suma/
    path('<int:numero1>/<int:numero2>/suma/', views.suma, name='suma'),
    # ex: localhost:8000/calculadora/41/58/resta/
    path('<int:numero1>/<int:numero2>/resta/', views.resta, name='resta'),
    # ex: localhost:8000/calculadora/89/25/multiplicacion/
    path('<int:numero1>/<int:numero2>/multiplicacion/', views.multiplicacion, name='multiplicacion'),
    # ex: localhost:8000/calculadora/100/5/division/
    path('<int:numero1>/<int:numero2>/division/', views.division, name='division'),
]