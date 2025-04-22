from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from Authentication.models import Profil
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import ProfileEditForm
from .forms import ProfileImageForm

def nav(request):
    return render(request, 'nav.html')


def home(request):
    profile = Profil.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # Rasm yuklash uchun request.FILES kerak
        if form.is_valid():
            form.save()
            return redirect('home')  # Post qo‘shilgach, sahifani qayta yuklash
    else:
        form = PostForm()

    posts = Post.objects.order_by('-created_at')  # Eng yangi postlar birinchi chiqishi uchun
    messages.success(request, 'Siz home sahifaga kirdingiz')


    return render(request, 'home.html', {'form': form, 'posts': posts, 'profile': profile})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Post mavjudligini tekshiramiz
    post.delete()
    return redirect('home')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Siz tizimga kirdingiz')
            return redirect('home')
        else:
            messages.error(request, 'Login yoki parol xato')
            return redirect('login')
        
    messages.success(request, 'Siz loginga kirdingiz')

    return render(request, 'login.html') 

def logout(request):
    auth_logout(request)

    messages.success(request, 'Siz logout bolimiga kirdingiz')

    return render(request, 'logout.html')

def edit_profile(request, pk):
    profile = get_object_or_404(Profil, pk=pk)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES,  instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


def update_profile_image(request):
    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profil)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileImageForm(instance=request.user.profile)
    return render(request, 'home.html', {'form': form})

def networks(request):
    return render(request, 'network.html')

def SnakeGame(request):
    return render(request, 'snake-game.html')

def CarGame(request):
    return render(request, 'car-game.html')

def LadderSnake(request):
    return render(request, 'ladder-snake.html')