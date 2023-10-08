from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('1/',views.blog1, name = 'blogs'),
    path('form/',views.showFormsData),
]