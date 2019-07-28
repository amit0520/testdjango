from django.urls import path

from . import views

urlpatterns = [
    path('', views.idb, name='idb')
]