from django.contrib import admin
from django.urls import path
from disp_data import views

app_name = 'disp_data'

urlpatterns = [
    path('', views.my_view, name='ourhome'),   
]