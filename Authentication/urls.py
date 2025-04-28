from  django.urls import path
from  .views import *

urlpatterns = [
    path('profile/', profil, name='profile'),
    path('register/', register, name='register'),
]


