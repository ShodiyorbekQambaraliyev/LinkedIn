from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from LinkedIn import views

urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/edit/<int:pk>/', edit_profile, name='edit_profile'),
    path('update-profile-img/', views.update_profile_img, name='update_profile_img'),
    path('networks/', networks, name='networks'),
    path('snake-game/', SnakeGame, name='snake-game'),
    path('car-game/', CarGame, name='car-game'),
    path('ladder-snake/', LadderSnake, name='ladder-snake'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)