from . import views
from django.urls import path

urlpatterns = [

    path('', views.login, name='login'),        
    path('addUser/', views.addUser, name='addUser'),        
    path('login/', views.login, name='login'),        
]