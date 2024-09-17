from django.shortcuts import get_object_or_404, redirect, render
from .models import Posteo
from .forms import PostForm
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
@login_required
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

@login_required
def Crear(request):
    if request.method == 'POST':
        form= PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('lista_posteos')
    else:
        form = PostForm()
        posts = Posteo.objects.exclude(author=request.user)
    return render(request,'post_manage.html', {'form':form, 'posts':posts})

@login_required
def post_list(request):
    posts = Posteo.objects.all().order_by('-Fecha_de_publicacion')  # Muestra los posts más recientes primero
    return render(request, 'posts.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Posteo, pk=pk)
    return render(request, 'post.html', {'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Posteo, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posteos')  # Redirige a la lista de posts después de eliminar
    return render(request, 'post.html', {'post': post})
