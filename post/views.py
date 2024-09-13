from django.shortcuts import get_object_or_404, redirect, render
from .models import Posteo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# AUTH
def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth.html', {'form': form, 'is_login':False})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth.html', {'form': form, 'is_login': True})

def user_logout(request):
    logout(request)  
    return redirect('login')  

def home(request): 
    return render(request, 'home.html')

# MANAGE POSTS

def EditarPost(request, pk):
    post= get_object_or_404(Posteo, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_manage.html', {'form':form})

def Crear(request):
    if request.method == 'POST':
        form= PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = Postform()
    return render(request,'post/post_manage.html', {'form':form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Muestra los posts más recientes primero
    return render(request, 'post/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  # Redirige a la lista de posts después de eliminar
    return render(request, 'post/delete_post.html', {'post': post})
