from django.urls import path,include
from . import views

app_name = "appointments"

urlpatterns = [

    path('dashboard', views.dashboard , name='dashboard'),
    # path('logout' , views.logout , name='logout' ),
    path('updateProfile/<int:pk>', views.UpdateProfile , name='UpdateProfile'),
    path('createSlots/<int:pk>', views.CreateSlots , name='CreateSlots'),
    path('bookAppointment', views.BookAppointment , name='BookAppointment'),
    path('ShowAvailable', views.ShowAvailable , name='ShowAvailable'),
    path('bookSlot/<int:pk>', views.bookSlot , name='bookSlot'),
    path('cancelAppointment/<int:pk>', views.cancelAppointment , name='cancelAppointment'),
    path('deleteAppointment/<int:pk>', views.deleteAppointment , name='deleteAppointment'),
]
