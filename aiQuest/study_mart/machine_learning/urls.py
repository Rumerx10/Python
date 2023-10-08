from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('ml',views.machine_learning, name='ml'),
    path('random/',views.random, name= 'rf'),
    path('knn/',views.knn, name= 'knn'),
    path('dt/',views.dt, name= 'dt'),
]