from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.register, name='register'),
    path('register-by-sector/<int:setor_pk>/', views.register_with_sector,
         name='register_with_sector'),
]
