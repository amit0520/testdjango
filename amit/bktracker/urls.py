from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('idb/', views.idb, name='idb'),
]