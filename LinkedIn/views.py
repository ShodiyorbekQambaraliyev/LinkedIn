from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm



def nav(request):
    return render(request, 'nav.html')

def home(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = PostForm()

    posts = Post.objects.order_by('-created_at') 
    return render(request, 'home.html', {'form': form, 'posts': posts})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('home')


def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')
