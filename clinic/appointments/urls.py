from django.urls import path,include
from . import views

app_name = "appointments"

urlpatterns = [

    path('dashboard', views.dashboard , name='dashboard'),
<<<<<<< HEAD
    path('updateProfile' , views.UpdateProfile , name = 'update' ),

=======
    path('updateProfile', views.UpdateProfile , name='UpdateProfile'),
>>>>>>> 741d2089af25c7394a33175b6ef3bcb184ff4a06

]
