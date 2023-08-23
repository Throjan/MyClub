from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('register/', views.register, name='register'),
    path('register/success', views.success, name='success'),
    path('success/', views.success, name='success'),
   
]