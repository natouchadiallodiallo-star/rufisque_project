from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('apropos/', views.apropos, name='apropos'),
    path('destinations/', views.destinations, name='destinations'),
    path('culture/', views.culture, name='culture'),
    path('nature/', views.nature, name='nature'),
    path('contact/', views.contact, name='contact'),
]