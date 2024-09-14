from django import forms
from .models import Posteo

class PostForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['titulo', 'contenido']  # Incluye los campos que deseas en el formulario

    # validaciones personalizadas:
    # def clean_titulo(self):
    #     titulo = self.cleaned_data.get('titulo')
    #     if 'invalid' in titulo:
    #         raise forms.ValidationError("El título contiene caracteres no válidos.")
    #     return titulo
