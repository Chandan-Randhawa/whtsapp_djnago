from django.contrib import admin
from django.urls import path 
from cmcapp import views

urlpatterns = [
    path('', views.sendwhtsappmessage , name = 'send whtsapp message'),

    path('indexx', views.indexx , name = 'indexx'),
    


]