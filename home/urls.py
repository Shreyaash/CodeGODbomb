from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('callbombindex', views.callbombindex,name='callbombindex'),

    path('docallattack/', views.docallattack,name="docallattack"),
    path('doattack/', views.doattack,name="doattack")

]