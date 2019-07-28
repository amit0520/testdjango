"""amit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path

from django.urls import path, include
# from .url import urlpatterns
urlpatterns = [
#    path('', include('cal.urls')),
#    path('', include('admin.urls')),
    path('', include('bktracker.urls')),
    path('idb/', include('bktracker.urls')),
    path('admin/', admin.site.urls),
]



# from django.db import models
#
# class BKrecords(models.Model):
#     t1 = models.IntegerField
#     t2 = models.IntegerField
#     t3 = models.IntegerField
#     t4 = models.IntegerField
#     t5 = models.IntegerField
#     t6 = models.IntegerField
#     plantID = models.CharField(max_length=10)
#     lineID = models.CharField(max_length=10)
#     timestamp = models.DateTimeField
#     bkTime = models.IntegerField
#
#     class Meta:
#         db_table = "bk_records"
