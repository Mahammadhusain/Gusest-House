from django.urls import path,include
from .views import login,logout,register,showuser,edituser,reset


urlpatterns = [
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('register/',register,name='register'),
    path('showuser/',showuser,name='showuser'),
    path('edituser/<int:id>',edituser,name='edituser'),
    path('reset/',reset,name='reset'),
]
