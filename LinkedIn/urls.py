from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/edit/<int:pk>/', edit_profile, name='edit_profile'),
    path('img_edit/<int:pk>/', img_edit, name='img/edit'),
    path('network/', network, name='network'),
    path('snake-game/', SnakeGame, name='snake-game'),
    path('car-game/', CarGame, name='car-game'),
    path('ladder-snake/', LadderSnake, name='ladder-snake'),
]
