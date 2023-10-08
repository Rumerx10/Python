from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', views.data_analysis),
    path('da/',views.data_analysis, name = 'data'),
    path('ia/',views.information_analysis),
    path('cls/',views.DataAnalysis.as_view())
]
