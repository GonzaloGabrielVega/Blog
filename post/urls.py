from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register ,name='register'),
    path('login/',views.user_login ,name='login'),
    path('logout',views.logout ,name='logout'),

    path('', views.home,name='home'),
    
    path('posts/',views.post_list, name='lista_posteos'),
    path('posts/<id>', views.post_detail, name='detalle_posteo'),
    path('posts/create', views.Crear, name='crear'),
    path('posts/<id>/delete', views.delete_post, name='delete'),
    path('posts/<id>/edit', views.EditarPost, name='edit'),
]
