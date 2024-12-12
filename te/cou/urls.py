from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('list/', courselist, name='list'),
    path('se/', ser_co, name='ser')
]