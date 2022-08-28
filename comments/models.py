import email
from tkinter import CASCADE
from django.db import models
from blog.models import Post
from django.utils import timezone


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    comentario = models.TextField(verbose_name='Comentario')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_comentario = models.DateField(default=timezone.now)
    publicado_coment = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_comentario