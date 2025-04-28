from django.shortcuts import render, redirect
from .models import Profil
from LinkedIn.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse


def profil(request):
    profil = Profil.objects.all()
    post = Post.objects.all()

    messages.success(request, 'Siz profilga kirdingiz')

    return render(request, 'profile.html', {'profil': profil, 'post': post})

def register(request):

    if request.user.is_authenticated:
        messages.success(request, 'Siz profilga kirdingiz')
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "Parollar mos kelmaydi!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bunday foydalanuvchi mavjud!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz va tizimga kirdingiz!")
            return redirect('home')

        messages.error(request, "Autentifikatsiyada xatolik yuz berdi!")
        return redirect('register')
    
    return render(request, 'register.html')




