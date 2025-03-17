from django.urls import path
from .views import home, delete_post, login, profile

urlpatterns = [
    path('home/', home, name='home'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
]
