from django.urls import path
from . import views

urlpatterns = [
    # auth
    path('register/',views.register ,name='register'),
    path('login/',views.user_login ,name='login'),
    path('logout/',views.user_logout ,name='logout'),

    # regular
    path('', views.home,name='home'),
    
    # navegation
    path('posts/',views.post_list, name='lista_posteos'),
    path('posts/<int:pk>', views.post_detail, name='detalle_posteo'),
    path('posts/create', views.Crear, name='crear'),
    path('posts/<pk>/delete', views.delete_post, name='delete'),
    path('posts/<pk>/edit', views.EditarPost, name='edit'),
]