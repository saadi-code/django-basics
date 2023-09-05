from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('abouttttt/', views.about, name='about'),
    path('service/', views.services, name='service'), 
    path('contact/', views.contact, name='contact')

   ]
