from django.urls import path
from . import views

urlpatterns = [
    path('lab-dashboard/', views.lab_dashboard, name='lab_dashboard'),
]
