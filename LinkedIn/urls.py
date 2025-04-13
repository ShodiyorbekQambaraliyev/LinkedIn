from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('snake-game/', SnakeGame, name='snake-game'),
    path('car-game/', CarGame, name='car-game'),
]
