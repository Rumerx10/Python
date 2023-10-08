from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('dlos/',views.deep_learning_os),
    # path('dlai',views.deep_learning_ai),
    path('dl/',views.deep_learning, name='dl'),
    path('register/', views.registration)
]