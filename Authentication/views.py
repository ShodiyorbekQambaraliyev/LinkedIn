from django.shortcuts import render, redirect
from .models import Profil
from LinkedIn.models import Post
from django.contrib import messages



def profil(request):
    profil = Profil.objects.all()
    post = Post.objects.all()

    messages.success(request, 'Siz profilga kirdingiz')

    return render(request, 'profile.html', {'profil': profil, 'post': post})

def register(request):
    return render(request, 'register.html')




