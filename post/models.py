from django.db import models
from django.contrib.auth.models import User

class Posteo(models.Model):
    titulo = models.CharField(max_length=120)
    contenido= models.TextField()
    Fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    autor= models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_manage')

    def __str__(self):
        return f"{self.titulo}... Fecha: {self.Fecha_de_publicacion}"