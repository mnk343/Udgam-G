from django.urls import path,include
from . import views

app_name = "appointments"

urlpatterns = [

    path('dashboard', views.dashboard , name='dashboard'),

    path('updateProfile/<int:pk>', views.UpdateProfile , name='UpdateProfile'),

]
